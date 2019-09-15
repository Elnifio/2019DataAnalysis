# Used to get all names in organized_data.txt
import json

def add_blank(str):
  str += '\n'
  return str

all_data = []
stock_names = []

with open('organized_data.txt', 'r') as f:
    all_data = f.read().split('\n')

for i in range(len(all_data) - 1):
        content = json.loads(all_data[i])
        stock_names.append(content['symbol'])

with open('valid_stock_names.txt', 'w') as f:
    for name in stock_names:
        f.write(add_blank(name))