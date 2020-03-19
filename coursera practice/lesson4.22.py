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
    r = requests.get(url,headers)
    # put the re expression on one line
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>&nbsp;<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span><\/td>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
# print(djidf)

#美股个股股票信息fromYahoo
def retrieve_quotes_historical(stock_code):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/{}/history?p={}'.format(stock_code,stock_code)
    r = requests.get(url,headers)
    search_pattern = re.compile('{"date":(15.*?),"open":(.*?),"high":(.*?),"low":(.*?),"close":(.*?),"volume":(.*?),"adjclose":(.*?)}')
    dji_list_in_text = re.findall(search_pattern,r.text)
    return dji_list_in_text

quotes_list = retrieve_quotes_historical('AXP')
quotesdf_or = pd.DataFrame(quotes_list)
quotesdf_or.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
# print(quotesdf_or)

# 修改个股dataframe的index 及去掉列
def date_func(x):
    a = datetime.strftime(x, '%Y-%m-%d')
    return a
date_orlist = map(int, pd.Series.to_list(quotesdf_or['date']))
# print(type(date_orlist))
date_cllist = list(map(date_func,map(datetime.fromtimestamp,date_orlist)))
# print(date_cllist)
quotesdf_or.index = date_cllist
quotesdf = quotesdf_or.drop(['date','adjclose'],axis =1 )



