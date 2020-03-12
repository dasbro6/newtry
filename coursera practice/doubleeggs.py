import sys
import time

sys.setrecursionlimit(3000)
dict_a = {}
def howmanyeggs(t,n):
    '''t = floors,n=eggs'''


    set_a = str([t,n])
    if n == 1:
        return t
    elif t == 1:
        return 1
    elif  set_a in dict_a:
        return dict_a[set_a]
    else:
        list_result=[]
        a = int(t/(n))
        for_n = max(a,2)
        print(for_n)
        for_n = t
        for k in range(1,for_n):
            floor_k = howmanyeggs(k,n-1)
            floor_tk = howmanyeggs(t-k,n)
            print('k= ',k,'floors =',t,floor_k,floor_tk)
            list_result.append(max(floor_k,floor_tk)+1)
        r = min(list_result)
        key = str([t,n])
        dict_a[key] = r

        return r

t = int(input('floors'))
n = int(input('eggs'))
start = time.time()
print('result:',howmanyeggs(t,n))
stop = time.time()


print(dict_a)
print(stop-start)