# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import requests
import re
from datetime import datetime

pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
start = datetime.now()
#美股个股股票信息fromYahoo
def retrieve_quotes_historical(stock_code):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/{}/history?p={}'.format(stock_code,stock_code)
    r = requests.get(url,headers)
    search_pattern = re.compile('{"date":(15[0-9]{8}),"open":(\d{1,}\.\d{1,}),"high":(.*?),"low":(.*?),"close":(.*?),"volume":(.*?),"adjclose":(.*?)}')
    dji_list_in_text = re.findall(search_pattern,r.text)
    return dji_list_in_text

quotes_list = retrieve_quotes_historical('DD')
stop1 =datetime.now()#插入一个计时节点

quotesdf_or = pd.DataFrame(quotes_list,dtype= float)
quotesdf_or.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
print(quotesdf_or)

# 修改个股dataframe的index 及去掉列
def date_func(x):
    a = datetime.strftime(x, '%Y-%m-%d')
    return a
date_orlist = list(map(int, pd.Series.to_list(quotesdf_or['date'])))
print(type(date_orlist[1]))
date_cllist = list(map(date_func,map(datetime.fromtimestamp,date_orlist)))
print(date_cllist)
quotesdf_or.index = date_cllist
quotesdf = quotesdf_or.drop(['date','adjclose'],axis =1 )
print(quotesdf)


print(len(quotesdf[(quotesdf.index >= '2019-09-01')&(quotesdf.index<='2019-09-30')]))
#涨的天数
print(len(quotesdf[quotesdf.close>quotesdf.shift().close]))
# print(len(quotesdf[quotesdf.close>quotesdf.open]))
#跌的天数
print(len(quotesdf[quotesdf.close<quotesdf.shift().close]))

print(type(quotesdf.close))
status = np.sign(np.diff(quotesdf.close))
print(len(status[status==1]))
print(len(status[status==-1]))

#
# #按月份分组
# month = [item[5:7] for item in quotesdf.index]
# quotesdf.groupby(month)
# print(quotesdf.groupby(month).apply(len))
# # print(quotesdf.groupby(month).groups)
# print(quotesdf.groupby(month).close.count())
# # for k,data in quotesdf.groupby(month):
# #     print (k,data)
#
# print(quotesdf.max(axis = 1))
# print(quotesdf.groupby(month).close.mean())
#
# stop2 =datetime.now()
# print("1",stop1-start,'2',stop2-stop1)