


# #举例子
# # from sklearn import linear_model
# # import numpy as np
# # import  matplotlib.pyplot as plt
# #
# # clf = linear_model.LinearRegression()
# # X = np.array([2,3,5,7,6]).reshape(-1,1)
# # y = np.array([6,10,14.5,21,18.5])
# # clf.fit(X,y) # 训练模型
# # b, a = clf.coef_, clf.intercept_
# # print(b, a)
# # x = [[4]]
# # print(clf.predict(x)) # 预测
# # plt.plot(X,a+b*X, color = 'red')
# # plt.show()

import  matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import pandas as pd

pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)


boston = datasets.load_boston()
X = pd.DataFrame(boston.data,columns = boston.feature_names)
y = pd.DataFrame(boston.target,columns = ['MEDV'])


#简要观察下数据
# print(X,y,X.shape)
# plt.subplot(2,1,1)
# plt.scatter(X['RM'], y, color='blue')
# plt.subplot(2,1,2)
# plt.scatter(X['LSTAT'], y, color='blue')
#
# plt.show()



import statsmodels.api as sm
# statsmodels 中的线性回归模型没有截距项，下行给训练集加上一列数值为 1 的特征

# print(X_add1)
X_add1 = sm.add_constant(X)
model = sm.OLS(y, X_add1).fit() # sm.OLS()为普通最小二乘回归模型，fit()用于拟合
print (model.summary())

# 移除两个属性/特征
X.drop('AGE', axis = 1, inplace = True)
X.drop('INDUS', axis = 1, inplace = True)
X_add2 = sm.add_constant(X)
model = sm.OLS(y, X_add2).fit()
print (model.summary())


# 假设测试数据如下：
X_test = np.array([[1, 0.006, 18.0, 0.0, 0.52, 6.6, 4.87, 1.0, 290.0,
15.2, 396.2, 5]]) # 第一个数 1 为同样添加的常数项

print(model.predict(X_test))
