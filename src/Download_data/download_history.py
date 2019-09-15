# Used to download historical datas to historical_data folder
import aiohttp
import asyncio

responses = []

all_names = []

# Access data for the first time, use valid_stock_names.txt as source of name
# with open('valid_stock_names.txt', 'r') as f:
#     all_names = f.read().split('\n')

# Access data for the second time, use invalid_historical_name.txt as source of name
with open('invalid_historical_name.txt', 'r') as f:
    all_names = f.read().split('\n')

async def fetch(name):
    # connect to the server
    async with aiohttp.ClientSession() as session:
        # create get request
        async with session.get('https://cloud.iexapis.com/stable/stock/{}/chart/1y?pk_639c5ae7fcf54fd9ad93f562cda67be1'.format(name)) as response:
            # wait for response
            response = await response.text()
            # responses.append(response)
            with open('historical_data/{}.txt'.format(name), 'w') as f:
                f.write(response)


def main():
    tasks =  []
    loop = asyncio.new_event_loop()
    for name in all_names:
        tasks.append(loop.create_task(fetch(name)))

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


main()