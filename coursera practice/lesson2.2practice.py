# -*- coding: utf-8 -*-

# 1. 使用以下语句存储一个字符串：
# string = 'My moral standing is: 0.98765'
# # 将其中的数字字符串转换成浮点数并输出

# string = 'My moral standing is: 0.98765'
# string_list = string.split(':')
# floatnum  = float(string_list[1])
# print(floatnum)

# # 2. 自定义函数move_substr(s, flag, n)，将传入的
# # 字符串s按照flag（1代表循环左移，2代表循环右移）的
# # 要求左移或右移n位（例如对于字符串abcde12345，循环左
# # 移两位后的结果为cde12345ab，循环右移两位后的结果为45abcde123），
# # 结果返回移动后的字符串，若n超过字符串长度则结果返回-1。
# # __main__模块中从键盘输入字符串、左移和右移标记以及移动的位数，
# # 调用move_substr()函数若移动位数合理则将移动后的字符串输出，
# # 否则输出“the n is too large”。
#
#
# def move_substr(s, flag, n):
#     if n > int(len(s)):
#         return -1
#     else:
#         if flag == 1:
#             return s[n:]+s[:n]
#         elif flag == 2:
#             return s[-n:]+s[:-n]
#         else:
#             print('flag must be 1 or 2 ')
#
#
# if __name__ == "__main__":
#     s, flag, n = input("enter the 'string,flag,n': ").split(',')
#     result = move_substr(s, int(flag), int(n))
#     print(result)
# else:
#     print('the n is too large')


# # 3.定义函数countchar()按字母表顺序统计字符串
# # 中26个字母出现的次数（不区分大小写）。例如字符串
# # “Hope is a good thing.”的统计结果为：
#
# def countchar(str):
#     str.lower()
#     alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#     # count_list=[0]*26
#     for char in str:
#         for alpha in char:
#             if alpha == char:
#                 index = alpha_list.index(alpha)
#                 count_list[index] += 1
#     return count_list
#
# if __name__ == "__main__":
#     str_a = input('input some string :')
#     print(countchar(str_a))


# 4. 从键盘输入整数n（1-9之间），对于1-100之间的整数删除包含n并且
# 能被n整除的数，例如如果n为6，则要删掉包含6的如6，16这样的数及
# 是6的倍数的如12和18这样的数，输出所有满足条件的数，要求每满10个
# 数换行。
# 测试数据：
# Enter the number: 6
# 屏幕输出：
# 1,2,3,4,5,7,8,9,10,11
# 13,14,15,17,19,20,21,22,23,25
# 27,28,29,31,32,33,34,35,37,38
# 39,40,41,43,44,45,47,49,50,51
# 52,53,55,57,58,59,70,71,73,74
# 75,77,79,80,81,82,83,85,87,88
# # 89,91,92,93,94,95,97,98,99,100

# def delnums(num):
#     hundred_list = list(range(1,101))
#     del_list = list(map(lambda x:x*num,range(1,int(100/num+1))))
#     return_list = list(set(hundred_list)-set(del_list))
#     return return_list
#
# if __name__ == "__main__":
#     num_del = int(input('Enter the number(1-9): '))
#     print(delnums(num_del))

# # 函数式编程思路
# s = input()
# i = int(s)
# num = list(map(str, filter(lambda x: x % i and s not in str(x), range(1, 101))))
# for i in range(0, len(num), 10):
#     print(','.join(num[i:i+10]))
#

# # 5. 请用随机函数产生500行1-100之间的随机整数
# # 存入文件random.txt中，编程寻找这些整数的众数
# # 并输出，众数即为一组数中出现最多的数。
#
# import random
#
# with open('random.txt','w+') as fp:
#     for i in range(500):
#         fp.write(str(random.randint(1,100)))
#         fp.write('\n')
#     fp.seek(0)
#     nums = fp.readlines()
# nums = [num.strip() for num in nums]
# setNums = set(nums)
# lst = [0] * 101
# for num in setNums:
#     c = nums.count(num)
#     lst[int(num)] = c
# for i in range(len(lst)):
#     if lst[i] == max(lst):
#         print(i)


# # 6. 文件article.txt中存放了一篇英文文章
# # （请自行创建并添加测试文本），假设文章中的
# # 标点符号仅包括“,”、“.”、“!”、“?”和“…”，编程
# # 找出其中最长的单词并输出。
#
# with open('article.txt') as fp:
#     data = fp.read()
# words = data.split()
# lst = []
# for word in words:
#     if word[-3:] == '...':
#         word = word[:-3]
#         lst.append(word)
#     if word[-1] in ',.?!':
#         word = word[:-1]
#     lst.append(word)
# result = sorted(lst, key = len, reverse = True)
# maxlen = len(result[0])
# # 最长单词可能不止一个且要去掉相同的单词
# for word in set(result):
#     n = len(word)
#     if n == maxlen:
#         print(word)
#
# num = 0
# for i in range(10):
#     num += (10**i)*5
#
# print(num%84)

# print([x**2 for x in range(5)])

# numbers = [5, 2, 1, 4,3, 6, 7, 8, 9, 10]
# X = numbers.sort()
# print(X)
#
# l = list('php')
# l[1:] ='ython'
# print(l)
# import math
# # # print((1,2) in zip(range(4),range(2,6)))
# # # x = [2,3,0,4,1]
# # # x.sort()
# # print('{:5.3f}'.format(math.pi))
# my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]
# print(my_list)
# print('short' in my_list)
# print(my_list[5])

# with open('test.txt', 'r+') as fp:
#     fp.seek(15)
#     print(fp.readline())
