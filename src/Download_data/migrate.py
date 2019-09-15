# Used to migrate data from earnings_data.txt to organized_data.txt
all_data = []
useful_data = []

def add_blank(str):
  str += '\n'
  return str

with open('earnings_data.txt', 'r') as f:
    all_data = f.read().split('\n')

print(all_data[-1])
print(all_data[1])


for item in all_data:
    if (item == all_data[1] or item == all_data[-1] or item == "Unknown symbol"):
      continue
    else:
        print(item)
        useful_data.append(item)

with open('organized_data.txt', 'w') as f:
    for item in useful_data:
        f.write(add_blank(item))