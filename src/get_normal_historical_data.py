# Organizes all historical data in Download_data
import os, sys, json

def get_path(name):
    return 'Download_data/historical_data/' + name

path = 'Download_data/historical_data/'
dirs = os.listdir(path)

for file in dirs:
    with open(get_path(file), 'r') as f:
        content = f.read()
        if content.split(',')[0] == '[{"date":"2018-08-15"':
            content = json.loads(content)
            with open('normal_historical_data/{}'.format(file), 'w') as f:
                for item in content:
                    f.write(json.dumps(item) + '\n')