class Athlete:
    def __init__(self, a_name, a_dob=None, a_records=[]):
        self.name = a_name
        self.dob = a_dob
        self.records = a_records

    def top3(self):
        return sorted(set(sanitize(each_data) for each_data in self.records))[0:3]

    def add_time(self, data):
        self.records.append(data)

    def add_times(self, data):
#        for each_data in data:
#            self.records.append(each_data)
        self.records.extend(data)

            
def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        spliter = '.'
        
    (mins, secs) = time_string.strip().split(spliter)
    return(mins + '.' + secs)



def get_files(file_name):
    try:
        with open(file_name, 'r') as name:
            data = name.readline()
            data_list = data.strip().split(',')
            the_object = {'name':data_list.pop(0),
                          'dob':data_list.pop(0),
                          'records': sorted(set(sanitize(each_data) for each_data in data_list))[0:3]
                          }
#            print(the_object)
            return(the_object)
#            return({'name':data_list.pop(0),'dob':data_list.pop(0),'records':sorted(set(sanitize(each_data) for each_data in data_list))[0:3]})
#            print(data_list)
#            the_name = data_list.pop(0)
#            the_date = data_list.pop(0)
#            print(the_name + ':' + the_date)
#            print(data_list)
            

#        return(sorted(set(sanitize(each_data) for each_data in data_list))[0:3])
        return(data_list)
    except IOError as ioe:
        print('IOError: ' + ioe)
        return(None)

def get_athlets(file_name):
    try:
        with open(file_name,'r') as file_data:
            data = file_data.readline()
            data_list = data.strip().split(',')
            return Athlete(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as ioe:
        print('IOError: ' + ioe)
        return(None)


#sarah = get_files('sarah2.txt')

"""
sarah = {}
data = get_files('sarah2.txt')
sarah['name'] = data.pop(0)
sarah['dob'] = data.pop(0)
sarah['records'] = sorted(set(sanitize(each_data) for each_data in data))[0:3]
"""

"""
print(sarah)
print(sarah['name'])
print(sarah['dob'])
print(sarah['records'])
"""

sarah = get_athlets('sarah2.txt')
print(sarah.name +'\'s ' +sarah.dob + ' is ' + str(sarah.top3()))

sarah.add_time('2.14')
print(sarah.name +'\'s ' +sarah.dob + ' is ' + str(sarah.top3()))

sarah.add_times(['2.11','2.01'])
print(sarah.name +'\'s ' +sarah.dob + ' is ' + str(sarah.top3()))



