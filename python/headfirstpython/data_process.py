def sanitize(time_string):
    if '-' in time_string:
        (mins, secs) = time_string.strip().split('-')
    elif ':' in time_string:
        (mins, secs) = time_string.strip().split(':')
    else:
        (mins, secs) = time_string.strip().split('.')

    return(mins + '.' + secs)



"""
Python sorting
"""

james = []
mikey = []
julie = []
sarah = []
#james
try:
    with open('james.txt', 'r') as james_file, open('julie.txt','r') as julie_file, open('mikey.txt', 'r') as mikey_file, open('sarah.txt','r') as sarah_file:
        data = james_file.readline()
        james_data = data.strip().split(',')
        for each_data in james_data:
            james.append(sanitize(each_data))
#        print(james)
        data = mikey_file.readline()
        mikey_data = data.strip().split(',')
        mikey = [sanitize(each_data) for each_data in mikey_data]
#        print(mikey)
        data = julie_file.readline()
        julie_data = data.strip().split(',')
        julie = [sanitize(each_data) for each_data in julie_data]
#        print(julie)
        data = sarah_file.readline()
        sarah_data = data.strip().split(',')
        sarah = sorted([sanitize(each_data) for each_data in sarah_data])
        print(sarah)
        
except IOError as ioe:
    print("Error: " + str(ioe))

print(sorted(james, reverse=False))
print(sorted(mikey))
print(sorted(julie))

"""
duplicate removal
"""
unique_sarah = []
for each_data in sarah:
    if(each_data not in unique_sarah):
        unique_sarah.append(each_data)
print(unique_sarah)

#sarah_set = set(sarah)
print(sorted(set(sarah))[0:3])
