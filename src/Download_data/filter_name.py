# Used to filter data that contains 'Exceeded...' or invalid data in historical_data
import os, sys

invalid_list = []

def get_path(name):
    return 'historical_data/' + name

path = 'historical_data/'
dirs = os.listdir(path)

for file in dirs:
    with open(get_path(file), 'r') as f:
        content = f.read().split(',')
        if content[0] != '[{"date":"2018-08-15"':
            invalid_list.append(file.split('.')[0])

with open('invalid_historical_name.txt', 'w') as f:
    for item in invalid_list:
        f.write(item + '\n')
