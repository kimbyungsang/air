import os

try:
    with open('man_data.txt') as man_data, open('other_data.txt') as other_data:
        print(man_data.readline())
        print(other_data.readline())
except IOError as err:
    print('File error :' + str(err))
