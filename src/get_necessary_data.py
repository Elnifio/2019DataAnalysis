import json, pandas, os, sys, re

def get_eps_surprise_dollar(stock_object_list):
    all_content = []

    def get_earnings(item):
        return item.get('earnings')[0].get('EPSSurpriseDollar', 'None')
    
    def get_fiscal_period(item):
        return item.get('earnings')[0].get('fiscalPeriod', 'None')

    with open('organized_data.txt', 'r') as f:
        all_content = f.read().split('\n')

    for item in all_content:
        if item != all_content[-1]:
            content = json.loads(item)
            for stock_object in stock_object_list:
                if stock_object['Name'] == content['symbol']:
                    stock_object['EPSSurpriseDollar'] = get_earnings(content)
                    stock_object['fiscalPeriod'] = get_fiscal_period(content)
                    break

    print("Finished getting EPS Surprise Dollar and Fiscal Period")


def get_all_delta_open(stock_object_list):
    path = 'normal_historical_data/'
    dirs = os.listdir(path)

    def get_path(name):
        return 'normal_historical_data/' + name

    def get_delta_content(item):
        all_content_json = []
        all_content = []
        with open(get_path('{}'.format(item)), 'r') as f:
            all_content_json = f.read().split('\n')
        
        for content in all_content_json:
            if content != all_content_json[-1]:
                data = json.loads(content)
                all_content.append(data)

        has_start_date = False
        has_end_date = False
        start_date_info = None
        end_date_info = None
        start_date_re = r'2019\-04'
        end_date_re = r'2019\-07'

        for content in all_content:
            date = content.get('date', 'None')
            if (re.match(start_date_re, date) and not has_start_date):
                start_date_info = content
                has_start_date = True
            if (re.match(end_date_re, date) and not has_end_date):
                end_date_info = content
                has_end_date = True

        delta_open = end_date_info.get('open') - start_date_info.get('open')
        return delta_open

    for file in dirs:
        file_name = file.split('.')[0]
        delta_open = get_delta_content(file)
        for stock_object in stock_object_list:
            if stock_object['Name'] == file_name:
                stock_object['delta_open'] = delta_open
                break
    
    print("Finished Processing historical open data")


def main():
    all_stocks_info = []
    all_names = []
    with open('valid_stock_names.txt', 'r') as f:
        all_names = f.read().split('\n')
    
    for name in all_names:
        if name != all_names[-1]:
            all_stocks_info.append({'Name': name, 'EPSSurpriseDollar': 'None', 'delta_open': 'None', 'fiscalPeriod': 'None'})

    get_eps_surprise_dollar(all_stocks_info)
    get_all_delta_open(all_stocks_info)

    valid_stocks_info = []

    for i in range(len(all_stocks_info) - 1):
        stock = all_stocks_info[i]
        if not (stock['EPSSurpriseDollar'] == 'None' or stock['delta_open'] == 'None' or stock['fiscalPeriod'] == 'None' or stock['fiscalPeriod'] == 'Q1 2019'):
            valid_stocks_info.append(stock)

    df = pandas.DataFrame(valid_stocks_info, columns=['Name', 'EPSSurpriseDollar', 'delta_open', 'fiscalPeriod'])
    df.to_csv('./overall_data.csv', index=False)


main()