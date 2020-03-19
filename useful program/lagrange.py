import pandas as pd
from scipy.interpolate import lagrange

with open('../coursera practice/test4_1.txt') as f:
    data = f.read()
    words = data.split()
#打开文件分割字符串

df = pd.DataFrame()
for i in range(1,5):
    dfcol = []
    for j in range(0,6):
        dfcol.append(words[i+j*5])
    df[i] = dfcol
#列表中元素写入list ，再将list写入DF

df_columms_list=['name','A','B','C']
df_columms_dict = {}
for i in range(0,4):
    df_columms_dict[i+1] =df_columms_list[i]
df.rename(columns = df_columms_dict,inplace= True)
#更换column 名称
# print(len(df))
# print(df['A'].isnull())
#



df1 = pd.read_excel('rawdata001.xlsx',sheet_name= 'Sheet2')

# print(df1)
# df_nona = df1.fillna(df1.max())
# print(df1_nona)



for i in df1.columns:
    for j in range(len(df)):
        if (df1[i].isnull())[j]:
            k = 3  # 设置取前后数的个数为3，默认为5
            y = df1[i][list(range(j - k, j)) + list(range(j + 1, j + 1 + k))] # 取数
            # print("for test",i,j,list(range(j - k, j)),list(range(j + 1, j + 1 + k)))
            # print('y.notnull()',y.notnull())
            y = y[y.notnull()]  # 去掉取出数中的空值
            print('y',y,"lagrange:", y.index, list(y))

            df1[i][j] = lagrange(y.index, list(y))(j)
print('df1',df1)