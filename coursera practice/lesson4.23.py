import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
from sklearn.cluster import KMeans
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
list7 = [88.0,89.0,87.0,86.0]
data = np.array([list1,list2,list3,list4,list5,list6,list7])
whiten = whiten(data)
centroids,_=kmeans(whiten,2)
result,_=vq(whiten,centroids)
print('result',result)

X = np.array([list1,list2,list3,list4,list5,list6,list7])
print(X)
KMeans = KMeans(n_clusters= 2).fit(X)
pred = KMeans.predict(X)
print('pred',pred)