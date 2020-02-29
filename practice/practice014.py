'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''


from math import sqrt

input = 900
prelist=[]
for i in range(2,input):
    panduan = 0
    sqrt_a=int(sqrt(i))
    for j in range(2,sqrt_a+1):
        if i%j == 0:
            panduan += 1
            break
    if panduan==0:
       prelist.append(i)
print(prelist)

fenjielist=[]
for k in prelist:
    print(k)
    if input%k == 0:
        input = input/k
        fenjielist.append(str(k))
        print(k)

print(fenjielist)

num = int(8954)
arr = []  # 质因数列表

tmp = num
while tmp != 1:
    pri = 2
    while pri != (num + 1):
        if (tmp % pri) == 0:
            tmp = tmp // pri
            arr.append(pri)
        else:
            pri += 1

exp = ' * '.join(map(str, arr))
print('%d = %s' % (num, exp))