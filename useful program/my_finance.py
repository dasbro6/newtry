# -*- coding: utf-8 -*-
import pandas as pd
import requests
import re
from datetime import datetime



#显示所有行、列
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

#dow 30股票信息fromCNN
def retrieve_dji_list():
    url ='http://money.cnn.com/data/dow30/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        r = requests.get(url,headers)
        # put the re expression on one line
        search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>&nbsp;<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span><\/td>')
    except ConnectionError as err:
            print(err)

    dji_list_in_text = re.findall(search_pattern, r.text)
    dij_list = []
    for item in dji_list_in_text:
        dij_list.append({'code': item[0], 'name': item[1],
                          'price': float(item[2])})
    return dij_list

# print(retrieve_dji_list())


#美股个股股票信息fromYahoo
def retrieve_quotes_historical(stock_code,start = '', end = ''):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/{}/history?p={}'.format(stock_code,stock_code)
    try:
        r = requests.get(url,headers)
        search_pattern = re.compile('{"date":(15[0-9]{8}),"open":(\d{1,}\.\d{1,}),"high":(.*?),"low":(.*?),"close":(.*?),"volume":(.*?),"adjclose":(.*?)}')
    except ConnectionError as err:
            print(err)
    quotes_list_in_text = re.findall(search_pattern,r.text)
    quotes_list =[]
    for item in quotes_list_in_text:
        quotes_list.append({'date': item[0], 'open': float(item[1]),
                          'high': float(item[2]),'low': float(item[3]),
                           'close': float(item[4]), 'volume': float(item[5]), 'adjclose': float(item[6])})
    return quotes_list

# print(retrieve_quotes_historical('MMM'))