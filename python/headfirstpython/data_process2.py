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
        return(sorted(set(sanitize(each_data) for each_data in data.strip().split(',')))[0:3])
    except IOError as ioe:
        print('IOError: ' + ioe)
        return(None)


print(get_files('james.txt'))
print(get_files('julie.txt'))
print(get_files('mikey.txt'))
print(get_files('sarah.txt'))
