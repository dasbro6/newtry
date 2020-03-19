# import pandas as pd
# # rawdata = pd.read_excel('rawdata001.xlsx')
# print(type(rawdata))
#
# rawdata['SUM'] = rawdata['Python']+rawdata['Math']
#
# print(rawdata)
#
# rawdata.to_excel('students.xlsx',sheet_name="scores")
#
# from sklearn import datasets
# iris = datasets.load_iris()
# # print(iris.data)
# irisdf = pd.DataFrame(data=iris.data)
# print(irisdf)
#
# # print(iris.feature_names())

#
# from nltk.corpus import brown
# import nltk
# # nltk.download()
# print(brown.fileids())



#
# # t = np.arange(0.,4.,0.1)
# # plt.plot(range(7),(4,2,4,4,1,5,7),'rD')
# # # print(t)
# # plt.show()
# # plt.savefig('test.jpg')
#
# printhelp(plt.plot())

#
# x = np.linspace(0, 1)
# y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
# print(x,y)
#
# plt.plot(x, y,'r--')
# plt.title('test jpg')
# plt.xlabel('XL')
# plt.ylabel('YL')
#
#
# plt.show()


# x = np.linspace(-np.pi,np.pi,300)
# #
# # plt.figure((1))
# # plt.subplot(211)
# # plt.plot(x,np.sin(x),color = 'r')
# # plt.subplot(212)
# # plt.plot(x,np.cos(x),color = 'g')
# # plt.show()

#
# x = np.linspace(-np.pi,np.pi,300)
# fig,(ax0,ax1) = plt.subplots(2,1)
# ax0.plot(x,np.sin(x),color = 'r')
# ax0.set_title('subplot1')
# plt.subplots_adjust(hspace = 0.5)
# ax1.plot(x,np.cos(x),color = 'g')
# ax1.set_title('subplot2')
# plt.show()
# import numpy as np
# # import matplotlib.pyplot as plt
# # x = np.linspace(-np.pi,np.pi,300)
# # plt.axes([.1,.1,0.8,0.8])
# # plt.plot(x,np.sin(x),color = 'r')
# # plt.axes([.3,.15,0.4,0.3])
# # plt.plot(x,np.cos(x),color = 'g')
# # plt.show()

#
# import pandas as pd
# from scipy.interpolate import lagrange
#
# with open('../coursera practice/test4_1.txt') as f:
#     data = f.read()
#     words = data.split()
# #打开文件分割字符串
#
# df = pd.DataFrame()
# for i in range(1,5):
#     dfcol = []
#     for j in range(0,6):
#         dfcol.append(words[i+j*5])
#     df[i] = dfcol
# #列表中元素写入list ，再将list写入DF
#
# df_columms_list=['name','A','B','C']
# df_columms_dict = {}
# for i in range(0,4):
#     df_columms_dict[i+1] =df_columms_list[i]
# df.rename(columns = df_columms_dict,inplace= True)
# #更换column 名称
# # print(len(df))
# # print(df['A'].isnull())
#



# df1 = pd.read_excel('rawdata001.xlsx',sheet_name= 'Sheet2')

# print(df1)
# df_nona = df1.fillna(df1.max())
# print(df1_nona)


#
# for i in df1.columns:
#     for j in range(len(df)):
#         if (df1[i].isnull())[j]:
#             k = 3  # 设置取前后数的个数为3，默认为5
#             y = df1[i][list(range(j - k, j)) + list(range(j + 1, j + 1 + k))] # 取数
#             # print("for test",i,j,list(range(j - k, j)),list(range(j + 1, j + 1 + k)))
#             # print('y.notnull()',y.notnull())
#             y = y[y.notnull()]  # 去掉取出数中的空值
#             print('y',y,"lagrange:", y.index, list(y))
#
#             df1[i][j] = lagrange(y.index, list(y))(j)
# print('df1',df1)


from sklearn import datasets
from sklearn import preprocessing
import pandas as  pd
import numpy as np
from sklearn.preprocessing import Binarizer

# #
# boston = datasets.load_boston()
# # # print(boston.data.shape)
# # # print(type(boston.feature_names))
# # print(boston.target)
# # #
# # print(boston.data)
#
# df = pd.DataFrame(boston.data)
# # df.columns = boston.feature_names[4:7]
# #
# print(df)

#

# dfcut1 =pd.cut(df.AGE[:20],5,labels=range(5))
# print(dfcut1)
#
# dfcut2=pd.qcut(df.AGE[:20],5,labels=range(5))
# print(dfcut2)

# X = boston.target.reshape(-1,1)
# print(X)
# Y = Binarizer(threshold=20.0).fit_transform(X)
# print(Y)

# from sklearn.decomposition import PCA
#
# X = preprocessing.scale(boston.data)
# pca = PCA(n_components= 5)
# print(pca.fit(X))
#
# print(pca.explained_variance_ratio_)
#
# pca_1 = PCA(n_components='mle')
# print(pca_1.fit(X))
# print(pca_1.explained_variance_ratio_)

data = np.random.randint(1,10,50)

import matplotlib.pyplot as plt
print(data)

# plt.show()

bins = np.linspace(data.min(),data.max(),3,endpoint = True)
print(bins)
plt.hist(data,bins = bins,rwidth = 0.95,edgecolor = 'k')
plt.show()