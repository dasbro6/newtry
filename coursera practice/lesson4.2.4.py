
# #三角函数画画图
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-np.pi,np.pi,256)
# s = np.sin(x)
# c = np.cos(x)
# plt.title('Trigonometric Function')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.plot(x,s)
# plt.plot(x,c)
# plt.show()

# #
# import scipy as sp
# import matplotlib.pyplot as plt
# listA =sp.ones(500)
# print(listA)
# listA[100:300]= -1
# f = sp.fft(listA)
# plt.plot(f)
# plt.show()


# from nltk.corpus import gutenberg
# # print(gutenberg.fileids())
# allwords = gutenberg.words('shakespeare-hamlet.txt')
# print(len(allwords))
# print(len(set(allwords)))
# print(allwords.count('Hamlet'))
# A = set(allwords)
# longwords = [w for w in A if len(w)>12]
# print(sorted(longwords))
#
#
from nltk.probability import *
# fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
# print(fd2.B())
# print(fd2.N())
# # fd2.tabulate(20)
# fd2.plot(20)
# # fd2.plot(20,cumulative = True)

from nltk.corpus import inaugural
fd3 = FreqDist([s for s in inaugural.words()])
print(fd3.freq('freedom'))

cfd = ConditionalFreqDist(
    (fileid,len(w))
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    if fileid>'1980' and fileid<'2010'
)
print(cfd.items())
cfd.plot()