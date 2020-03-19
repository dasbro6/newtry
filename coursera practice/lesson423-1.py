import pandas as pd
import numpy as np
import requests
import re
from datetime import datetime
import time
from sklearn.cluster import KMeans

#美股个股股票信息fromYahoo
def retrieve_quotes_historical(stock_code):
    start = datetime.now()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/{}/history?p={}'.format(stock_code,stock_code)
    r = requests.get(url,headers)
    search_pattern = re.compile('{"date":(15[0-9]{8}),"open":([0-9].*?),"high":(.*?),"low":(.*?),"close":(.*?),"volume":(.*?),"adjclose":(.*?)}')
    dji_list_in_text = re.findall(search_pattern,r.text)
    quotes_list = dji_list_in_text
    quotesdf_or = pd.DataFrame(quotes_list,dtype= float)
    quotesdf_or.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
    # 修改个股dataframe的index 及去掉列
    def date_func(x):
        a = datetime.strftime(x, '%Y-%m-%d')
        return a
    date_orlist = map(int, pd.Series.to_list(quotesdf_or['date']))
    # print(type(date_orlist))
    date_cllist = list(map(date_func,map(datetime.fromtimestamp,date_orlist)))
    # print(date_cllist)
    quotesdf_or.index = date_cllist
    quotesdf= quotesdf_or.drop(['date','adjclose'],axis =1 )

    stop1 =datetime.now()#插入一个计时节点
    print('查询股票{}用时{}'.format(stock_code,stop1-start))
    # time.sleep(5)
    return quotesdf

listDji = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD']
# listDji = ['MMM','AAPL','BA']
# listDji = ['KO','DIS','DD']
listTemp = [0]*len(listDji)
print(listTemp)
for i in range(len(listTemp)):
    listTemp[i] = retrieve_quotes_historical(listDji[i]).close
print(listTemp)

status= [0]*len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
    print(len(status[i]))

print(status)
kmeans =KMeans(n_clusters=3).fit(status)
pred = kmeans.predict(status)
print(pred)



