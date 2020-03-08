# x = int(input('X = '))
# y = int(input('Y = '))
# if x < y:
#     x,y=y,x
# while x % y !=0:
#     r = x % y
#     x = y
#     y = r
#
# print(y)
# #辗转相除法

#
# x = 1
# y = 2
# z = 5
# count=0
# for i in range(21):
#     for j in range(51):
#         for k in range(101):
#             if i*z+j*y+k*x == 100:
#                 count += 1
# print(count)
#

#
# i = 1
# while i % 3:
#     print(i, end = ' ')
#     if i >= 10:
#         break
#     i += 1
#
# for i in range(1, 10, 2):
#     if i % 5 == 0:
#         print("Bingo!")
#         break
# else:
#     print(i)

# count = []
# def hanoi (a,b,c,n):
#     if n == 1 :
#         print(a,'->',c)
#         count.append(1)
#     else:
#         hanoi(a,c,b,n-1)
#         print(a,'->',c)
#         count.append(1)
#         hanoi(b,c,a,n-1)
#     return
#
# hanoi("a","b","c",32)
# print(len(count))
# numA = int(input())
# numB = int(input())
# def foo(num,base):
#     if num >= base:
#         foo(num // base, base)
#         print(num%base, end='')
#
#
# foo(numA, numB)

# import math
#
# math.ceil(3.6)
# import random
# print(random.choice(['霸道总裁风', '冷艳高贵风', '扎心了老铁风', '人来风']))

# import datetime
#
# dt= datetime.datetime.now()
# print(dt)

while True:
    try:
        num1 = int(input('1: '))
        num2 = int(input('2: '))
        print(num1/num2)
        break
    except ValueError as exc:
        print('input nums')
        print(exc)
    except ZeroDivisionError as exc:
        print('num2 can not be 0')
        print(exc)
    else :
        print('good')