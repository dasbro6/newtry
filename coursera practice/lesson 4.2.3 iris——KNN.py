

# 2. 请参考scikit-learn官网（http://scikit-learn
# .org）或本周课程中的代码或其他资源尝试用经典的分类学习
# 算法KNN最近邻（k-nearest neighbor ，最简单的分类算法，
# 新的观测值的标签由n维空间中最靠近它的训练样本标签确定）
# 判断萼片长度和宽度、花瓣长度和宽度分别
# 是5.0cm, 3.0cm, 5.0cm, 2.0cm的鸢尾花所属类别。


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import confusion_matrix

 
print(iris.data.shape)
# knn = KNeighborsClassifier()
# # 从已有数据中学习
# knn.fit(iris.data, iris.target)
# # 利用分类模型进行未知数据的预测（确定标签）
# print(knn.predict([[5.0, 3.0, 5.0, 2.0]]))

#
# #划分训练集和测试集
# X = iris.data
# y = iris.target
# print(X)
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2)
#
# # 数据预处理
# X_train = scale(X_train)
# X_test = scale(X_test)
# # print(X_train,X_test)
#
# #创建模型
# knn = KNeighborsClassifier(n_neighbors=5)
#
# #模型拟合
# knn.fit(X_train, y_train)
#
# # 预测
# y_pred = knn.predict(X_test)
#
# # 评估
# print(confusion_matrix(y_test,y_pred))
#
# # 利用分类模型进行未知数据的预测（确定标签）
# print(knn.predict([[5.0, 3.0, 5.0, 2.0]]))