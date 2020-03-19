from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import scipy

iris = datasets.load_iris()

iris_df = pd.DataFrame(iris.data)
# print(iris_df)
iris_df.columns = iris.feature_names
# print(iris_df)
iris_df['target'] = iris.target
# print(iris_df)
# print(iris_df.target)
# iris_df.target.astype(float)
print(iris_df)


# plt.hist(iris_df.iloc[:,0],30,color='r')
# plt.hist(iris_df.iloc[:,1],30,color='r')
# plt.hist(iris_df.iloc[:,2],30,color='r')
# plt.hist(iris_df.iloc[:,3],30,color='r')
# plt.show()

# print(scipy.stats.normaltest(iris_df.iloc[:,0],axis =0))
# # 0.05是正态分布的阈值
# print(scipy.stats.normaltest(iris_df.iloc[:,1],axis =0))
# print(scipy.stats.normaltest(iris_df.iloc[:,2],axis =0))
# print(scipy.stats.normaltest(iris_df.iloc[:,3],axis =0))


# print(iris_df.target.value_counts())
#
# # iris_df.target.value_counts().plot(kind = 'pie')
# # plt.show()
#
# print(iris_df.iloc[:,0].mean())
#
# print(iris_df.iloc[:,0].median())
# # 标准差
# print(iris_df.iloc[:,0].std())
# # 分位值
# print(iris_df.iloc[:,0].quantile([0.25,0.75]))

# 基本信息
print(iris_df.iloc[:,0].describe())
# print(iris_df.iloc[:,0].describe().loc['75%']-iris_df.iloc[:,0].describe().loc['25%'])
# iris_df.plot.scatter(x =1 ,y =2)
# plt.show()

# X = [item[0] for item in iris.data]
# Y = [item[2] for item in iris.data]
# print(X)
# plt.scatter(X[:50],Y[:50])
# plt.show()


# # 计算相关性系数
# print(iris_df.iloc[:,[0,1,4,]].corr())
#
# print(iris_df['target'].corr(iris_df.iloc[:,0]))
#
#
# import seaborn as sns
#
# sns.heatmap(iris_df.iloc[:,[0,1,4,]].corr(),annot = True,fmt='1f' cmap='coolwarm')
# plt.show()