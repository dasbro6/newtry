'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

import time

def timelog(func):
    def wrapper_func():
        start=time.time()
        runfunc=func()
        end=time.time()
        print(end-start)

    return wrapper_func()

@timelog
def func_a():
    count=0
    for a in range(101,20000):
        i = 0
        for b in range(2,a-1):
            if a%b == 0:
                i += 1
                break
        if i == 0:
           print(a)
           count += 1

    print("合计数：",count)

@timelog
def func_b():
    from math import sqrt

    min = 101
    max = 20000

    prime = list()

    for i in range(min, max + 1):
        temp = int(sqrt(i))
        flag = True  # 是否为素数
        for j in range(2, temp + 1):
            if (i % j) == 0:
                flag = False
                break
        if flag == True:
            prime.append(i)

    print('%d-%d 之间共有 %d 个素数' % (min, max, len(prime)))
    print(prime)