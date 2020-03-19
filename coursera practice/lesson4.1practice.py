# # 1.
#
# import pandas as pd
# import matplotlib.pyplot as plt
# pdread = pd.read_excel('score.xlsx')
# df = pd.DataFrame(pdread)
# print(df)
# df.boxplot()
# plt.show()
#

# 利用Tushare包中的接口函数获取招商银行（股票代码600036）
# 2019年第一季度的股票数据并完成如下数据处理和分析任务：
# 1. 数据只保留date、open、high、close、low和volume这几个属性，
# 并按时间先后顺序对数据进行排序；
# 2. 选择2019年一季度和1月该股票最高价high和最低价low数据。
# 3. 输出这一季度内成交量最低和最高那两天的日期和分别的成交量；
# 4. 列出成交量在100000以上的记录；
# 5. 计算这一季度中收盘价（close）高于开盘价（open）的天数；
# 6. 计算前后两天开盘价的涨跌情况，用两种方式表示，
# 第一种输出每两天之间的差值（后一天减去前一天），
# 第二种输出一个开盘价涨跌列表，涨用1表示，
# 跌用-1表示；[提示：可使用diff()方法和sign()函数]
# 7. 绘制2019年1月该股票最高价high和最低价low的折线图；
# 8. 绘制该股票在此季度内每日收盘价与开盘价之差与当日成交量之间的散点图。
import pandas as pd
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

raw_data = ts.get_hist_data('600036',start='2019-01-01',end='2019-03-31')

# 1)
data_fiveC = pd.DataFrame.sort_index(pd.DataFrame(raw_data,columns =['open','high','close','low','volume']))


high_s =data_fiveC.high.sort_values(ascending=False)
high_list = high_s.to_list()[0:2]
trya = data_fiveC[data_fiveC['high'].isin(high_list)]
print(type(high_s),type(high_list),'high_list:',high_list)
print(trya)
# one way show highest 2 nums in columns'high',and print the row in DataFrame

#2)
print(pd.DataFrame(data_fiveC,columns = ['high','low']))
print(data_fiveC[['high','low']])
# season one
print(data_fiveC.loc['2019-01-02':'2019-01-31',['high','low']])
# January

# 3)
volume_s_max = data_fiveC.volume.sort_values(ascending=False)
max_day = volume_s_max[:2]
max_day_vol =max_day.values
max_day_date = max_day.index

print(type(volume_s_max))
print("the min volume of {} is at {}".format(max_day_vol,max_day_date))


# 4)
print(type(data_fiveC['volume']>1000000),type(data_fiveC.volume>1000000))


print(data_fiveC[data_fiveC['volume']>1000000])
print(data_fiveC.loc[data_fiveC.volume>1000000])


# 5)
print("5:",len(data_fiveC[data_fiveC['close']>data_fiveC['open']]))

# 6.1)
print("6.1:",data_fiveC.open.diff())
# 6.2)
print(np.sign(np.diff(data_fiveC.open)))

# 7)

data_fiveC.loc['2019-01-02':'2019-01-31',['high','low']].plot.line()


# 8)

df_x = pd.DataFrame(data_fiveC['close']-data_fiveC['open'])
df_x.columns =['CO']
df_x['volume'] = data_fiveC['volume']

print(df_x.describe())
# df_x.plot.scatter(x ='CO', y ='volume')
# # plt.show()