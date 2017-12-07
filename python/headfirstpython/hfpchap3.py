import os

man = []
other = []

try:
    data = open('hfp/code/chapter3/sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if(role == 'Man'):
                man.append(line_spoken)
            elif(role == 'Other Man'):
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

"""
try:

    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    print(man, file=man_file)
    print(other, file=other_file)

    man_file.close()
    other_file.close()
except IOError as err:
    print('File error: ' + str(err))
"""

"""
try:
    with open('man_data.txt','w') as man_file, open('other_data.txt','w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)

except IOError as err:
    print("Error :"+str(err))
"""
import pickle
try:
    with open('man_data2.txt', 'wb') as man_file, open('other_data2.txt','wb') as other_file:
        pickle.dump(man,file=man_file)
        pickle.dump(other,file=other_file)
except pickle.PickleError as perr:
    print("Error :" + str(perr))

import nester
try:
    with open('man_data2.txt', 'rb') as my_data, open('other_data2.txt', 'rb') as my_data2:
        man_data = pickle.load(my_data)
        other_data = pickle.load(my_data2)
        nester.print_lol(man_data)
        print('second file')
        nester.print_lol(other_data)
except pickle.PickleError as perr:
    print("Error: "+ str(perr))
