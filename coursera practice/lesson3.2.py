import numpy as np
from scipy import linalg



# aArray = np.ones((3,4))
# print(aArray)
# print(help(np.ones))


# bArray = np.array([[1,2],[3,4]])
# print(bArray)
# print(linalg.det(bArray))


import matplotlib.pyplot as plt
#
#
# np.random.seed(19680801)
# data = np.random.randn(2, 100)
#
# fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])
#
# plt.show()


# x = np.array([(1,2,3),(4,5,6)])
# print(x.ndim)
# print(x.shape)
# print(x.size)
#
# print(np.arange(1,10,0.5))

#
# a = np.arange(1, 5, dtype=np.float64)
# print(a)
# print(np.power(a, 2).sum())
#
# print(np.add(a, np.arange(4)))

#
# x = np.full((10,10),np.pi)
# x[1:-1,1:-1] = 0
#

# y = np.identity(10)
# # x = np.array([[1,2,3],[4,5,6]],dtype = np.float64)
# # print(x)
# # y = np.full_like(x,4)
# print(y)

# x = np.eye(10,k=-2)
# print(x)

# x = np.random.normal(0,5,100)
# print(x)

# x = np.random.uniform(-5,5,100)
# print(x)

# y = np.arange(1,100)
# # print(y)
# # # mask = np.random.choice(np.arange(y.shape[0]),2,replace= True)
# # # print(y[mask])
# # print(y[(y>50)&(y%2 == 0)])
# # # y[y % 2 == 0] = -1
# # # print(y)
# # print(np.where(y % 2 == 0,-1,y))

scores = np.array([[98,76,87],[76,88,91]])
score_mean = scores.mean(axis = 1,keepdims= True)
print(scores-score_mean)
print(score_mean)
