min=100
max=1000

for i in range(min,max):
    stri=str(i)
    lista=[]

    for j in stri:
        lista.append(j)

    # print(list,list[0],list[1],list[2])
    num=int(lista[0])**3+int(lista[1])**3+int(lista[2])**3
    if num == i:
        print(num)

'''
题目：打印出所有的"水仙花数"
'''

arr = list()

for i in range(100, 1000):
    a = int(i / 100) % 10
    b = int(i / 10) % 10
    c = int(i / 1) % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        arr.append(i)

print('水仙花数：' + str(arr))