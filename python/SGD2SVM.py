
# coding: utf-8

# In[1]:


import os, time, csv
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csr_matrix


# In[6]:


def explore(target_file, separator=',', fieldnames=None, binary_features=list(), numeric_features=list(), max_rows=20000):
    """
    Create MinMaxScaler and DictVectorizer from online stream
    
    Parameters:
    target file: stream file
    separator: delimiter
    fieldnames: field label (optional)
    binary_features: list of qualitative features
    numeric_features: list of numeric features
    max_rows: a number of row from stream file (None is possible)
    """
    features = dict()
    min_max = dict()
    vectorizer = DictVectorizer(sparse=False)
    scaler = MinMaxScaler()
    with open(target_file, 'r') as R:
        iterator = csv.DictReader(R, fieldnames, delimiter=separator)
        for n, row in enumerate(iterator):
            #data exploration
            for k,v in row.items():
                if k in binary_features:
                    if k+'_'+v not in features:
                        features[k+'_'+v] = 0
                elif k in numeric_features:
                    v = float(v)
                    if k not in features:
                        features[k] = 0
                        min_max[k] = [v,v]
                    else:
                        if v < min_max[k][0]:
                            min_max[k][0] = v
                        elif v > min_max[k][1]:
                            min_max[k][1] = v
                else:
                    pass
            if max_rows and n > max_rows:
                break

    vectorizer.fit([features])
    A = vectorizer.transform([{f:0 if f not in min_max else min_max[f][0] for f in vectorizer.feature_names_},                            {f:1 if f not in min_max else min_max[f][1] for f in vectorizer.feature_names_}])
    scaler.fit(A)
    return vectorizer, scaler

    


# In[17]:


def pull_examples(target_file, vectorizer, binary_features, numeric_features, target, min_max=None, separator=',',                  fieldnames=None, sparse=True):
    """
    return generator from online stream
    """
    with open(target_file, 'r') as R:
        iterator = csv.DictReader(R, fieldnames, delimiter=separator)
        for n, row in enumerate(iterator):
            
            #data processing
            stream_row = {}
            response = np.array([float(row[target])])
            for k,v in row.items():
                if k in binary_features:
                    stream_row[k+'_'+v]=1.0
                else:
                    if k in numeric_features:
                        stream_row[k] = float(v)
            if min_max:
                features = min_max.transform(vectorizer.transform([stream_row]))
            else:
                features = vectorizer.transform([stream_row])
            if sparse:
                yield(csr_matrix(features),response,n)
            else:
                yield(features, response, n)


# In[18]:


source = '/datasets/bikesharing/hour.csv'
local_path = os.getcwd()
b_vars = ['holiday', 'hr', 'mnth', 'season', 'weathersit', 'weekday', 'workingday', 'yr']
n_vars = ['hum', 'temp', 'atemp', 'windspeed']
std_row, min_max = explore(target_file=local_path+'/'+source, binary_features=b_vars, numeric_features=n_vars)
print('Feature: ')
for f,mv,mx in zip(std_row.feature_names_, min_max.data_min_, min_max.data_max_):
    print('%s:[%0.2f,%0.2f] ' %(f,mv,mx))


# In[24]:


from sklearn.linear_model import SGDRegressor
SGD = SGDRegressor(loss='epsilon_insensitive', epsilon=0.001, penalty=None, random_state=1, average=True)
val_rmse = 0
val_rmsle = 0
predictions_start = 16000

def apply_log(x): return np.log(x + 1.0)
def apply_exp(x): return np.exp(x) - 1.0

for x,y,n in pull_examples(target_file=local_path+'/'+source, vectorizer=std_row,                           min_max=min_max, binary_features=b_vars, numeric_features=n_vars, target='cnt'):
    y_log = apply_log(y)
    #machine learning
    if (n+1) >= predictions_start:
        #holdout after N phase
        predicted = SGD.predict(x)
        val_rmse += (apply_exp(predicted)-y)**2
        val_rmsle += (predicted - y_log)**2
        if(n-predictions_start+1)% 250 == 0 and (n+1) > predictions_start:
            print(n, end='')
            print('%s holdout RMSE: %0.3f' % (time.strftime('%X'), (val_rmse/float(n-predictions_start+1))**0.5), end='')
            print('holdout RMSLE: %0.3f'%((val_rmsle/float(n-predictions_start+1))**0.5))
    else:
        #learning phase
        SGD.partial_fit(x,y_log)
print('%s FINAL holdout RMSE: %0.3f' % (time.strftime('X'), (val_rmse/float(n-predictions_start+1))**0.5))
print('%s FINAL holdout RMSLE: %0.3f' % (time.strftime('X'), (val_rmsle/float(n-predictions_start+1))**0.5))


# In[28]:


source = 'datasets/shuffled_covtype.data'
local_path = os.getcwd()
n_vars = ['var_'+'0'*int(j<10)+str(j) for j in range(54)]
std_row, min_max = explore(target_file=local_path+'/'+source, binary_features=list(),                            fieldnames=n_vars+['covertype'], numeric_features=n_vars,                           max_rows=50000)
print('Feature: ')
for f,mv,mx in zip(std_row.feature_names_, min_max.data_min_, min_max.data_max_):
    print('%s:[%0.2f,%0.2f]' % (f,mv,mx))


# In[33]:


from sklearn.linear_model import SGDClassifier
SGD = SGDClassifier(loss='hinge', penalty=None, random_state=1, average=True)
accuracy = 0
accuracy_record = list()
predictions_start = 50
sample = 5000
early_stop = 50000

for x,y,n in pull_examples(target_file=local_path+'/'+source, vectorizer=std_row, min_max=min_max,                           binary_features = list(), numeric_features=n_vars, 
                           fieldnames=n_vars+['covertype'], target='covertype'):
    #learning phase
    if n>predictions_start:
        accuracy += int(int(SGD.predict(x))==y[0])
        if n % sample == 0:
            accuracy_record.append(accuracy/float(sample))
            print('%s Progressive accuracy at example %i: %0.3f' % (time.strftime('%X'), n, np.mean(accuracy_record[-sample:])))
            accuracy = 0
    if early_stop and n >= early_stop:
        break
    SGD.partial_fit(x,y,classes=range(1,8))
            

