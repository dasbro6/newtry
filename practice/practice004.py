'''
题目：输入某年某月某日（yyyy-MM-dd），判断这一天是这一年的第几天？
'''

shuru=input("输入某年某月某日",)

date=shuru.split('-')

y=int(date[0])
m=int(date[1])
d=int(date[2])

print(y,m,d)

arr=[31,29,31,30,31,30,31,31,30,31,30,31]

day=0
if y%4==0:
   for i in range(m):
        day+=arr[i-1]
   resulta=day+d
else:
    arr.remove(29)
    arr.insert(1,28)
    for i in range(m):
        day += arr[i - 1]
    resulta = day + d

print(resulta )