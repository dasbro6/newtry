
from sklearn.cluster import KMeans
from sklearn import datasets


#加载数据
iris = datasets.load_iris()
KMeans = KMeans(n_clusters= 3).fit(iris.data)
pred = KMeans.predict(iris.data)
# print('pred',pred)

for label in pred:
    print(label, end = ' ')    # 打印预测出的各条数据的标签
print('\n')
for label in iris.target:
    print(label, end = ' ')    # 打印原始标注好的正确标签