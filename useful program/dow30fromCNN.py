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
djidf = pd.DataFrame(dji_list,dtype= float)
djidf.columns = ['code','name','price']


print(djidf)
print(djidf.price.mean())
print(djidf[(djidf.price >= 300) | (djidf.price <=50)].name)

#排序
tempdf = djidf.sort_values(by = 'price',ascending=False)
print(tempdf.name[:3])