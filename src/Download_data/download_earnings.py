# Used to download earnings to earnings_data.txt
import aiohttp
import asyncio
import pandas
import json

responses = []

def add_blank(str):
  str += '\n'
  return str

with open('earnings_data.txt', 'w') as f:
    pass

async def fetch(url):
    # connect to the server
    async with aiohttp.ClientSession() as session:
        # create get request
        async with session.get(url) as response:
            # wait for response
            response = await response.text()
            responses.append(response)

cl = pandas.read_csv('companylist.csv')

def main():
    i = 0
    while i < 3508:
        try:
            try:
                stock_names = cl['Symbol'].loc[i:i + 9]
            except KeyError as e:
                stock_names = cl['Symbol'].loc[i:]
            tasks =  []
            loop = asyncio.new_event_loop()
            for name in stock_names:
                tasks.append(loop.create_task(fetch('https://cloud.iexapis.com/stable/stock/{}/earnings?token=pk_0d3e3c7445284c8c8f482a9a5e7c0eea'.format(name))))

            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()
        except ValueError as e:
            print("Except:", e)
        finally:
            i += 10


# stock_names = cl['Symbol'].loc[:10]
# tasks =  []
# loop = asyncio.new_event_loop()
# for name in stock_names:
#   tasks.append(loop.create_task(fetch('https://cloud.iexapis.com/stable/stock/{}/earnings?token=pk_4d5454432f7f4e3a870b432445ecf86a'.format(name))))

# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

main()

with open('earnings_data.txt', 'a') as f:
    for earning in responses:
        f.write(add_blank(earning))
