#-*-coding:utf-8-*-


#  # 1.BMI
# list=[18.5,24,28]
# weight = float(input('Your weight: '))
# high = float(input('Your high: '))
# BMI=weight/(high**2)
# print("Your BMI= ",BMI)
# if BMI>=list[2]:
#     print('fat')
# elif BMI>=list[1]:
#     print('overweigh')
# elif  BMI>=list[0]:
#     print('normal')
# else:
#     print('thin')

# # 2.F to C
# C = 0
# for F in range(0,301,20):
#     C = 5/9*(F-32)
#     print('F {} = C {}'.format(F,C))

# 3.gujiao

# x=int(input('int'))
# def gujiao(n):
#     print(n)
#     if n==1:
#         print('end')
#     elif n%2 ==0:
#         gujiao(n/2)
#     else:
#         gujiao(n*3+1)
#
# result_gujiao=gujiao(x)


# 4.���Ʒ� �׳�

# x = int(input('enter a int: '))
#
# def func(n):
#
#     if n == 1:
#         r = 1
#     elif n == 2:
#         r = n*(n-1)
#
#     else:
#         r=func(n-1)
#         r=n*r
#     return r
# s = 0
# for i in range(1,x+1):
#     s = s + func(i)
# print(s)

# # 5.���ظ���λ��
# list_num = []
# for i in range(1,5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != k and i != j and j != k:
#                 list_num.append(i*100+j*10+k)
# print(list_num)
# print(len(list_num))

# 6.��֤���⣺���һ����λ������37�ı��������������ѭ�����ƺ�õ���������3λ��Ҳ��37�ı�����
# for i in range(100,1000):
#
#     if i % 37 == 0:
#         print(i)
#         print((i//10+i%10*100) % 37 == 0)
#         print((i%100*10+i//100) % 37 == 0)

# for num in range(100, 1000):
#     if num % 37 == 0:
#         num_new_1 = num % 100 *10 + num // 100
#         num_new_2 = num % 10 * 100 + num // 10
#         if num_new_1 % 37 != 0 or num_new_1 % 37 != 0:
#             print("It's a false proposition.")
#             break
# else:
#     print("It's a true proposition.")

# 7. һ�������������������֮����������Ϊ����������6��6=1+2+3����̼���1000֮�ڵ����������������
# list_yinzi = []
# # # def func(n):
# # #     for i in range(1,n):
# # #         if n == 1:
# # #             list_yinzi.append(i)
# # #
# # #         elif n % i == 0:
# # #             list_yinzi.append(i)
# # #             func(n/i)
# # #         else:
# # #             return list_yinzi
# # #
# # # func(1000)
# # # print(list_yinzi)

# for i in range(1, 1001):
#    # ע��s��ֵ��λ�ã��账�õ�λ�ø�����Ҫ��������һ����������ѭ��������
#    s = 0
#    for j in range(1, i):
#        if i%j == 0:
#             s += j
#    if s == i:
#        print("\n", i, " ", end = "")
#        print("its factors are ", end = "")
#        for j in range(1, i):
#           if i%j == 0:
#               print(j, end = " ")


# 8.��֤��°ͺղ���֮һ��2000���ڵ���ż�������ڵ���4�����ܹ��ֽ�Ϊ��������֮�͡�ÿ��ż���������磺4=2+2����ʽ

#
from math import sqrt
n = int(input('input n :'))

zhishu = []
for j in range(2,n):

    zhishu.append(j)

    for k in range(2,int(sqrt(j)+1)):

        if j % k == 0:

            zhishu.remove(j)
            break

print(zhishu)
zhishu_r = list(reversed(zhishu))
# ��תһ���б�
print(zhishu_r)


list_main = list(range (4,n,2))
list_comp = []



def yanzheng(x):

    for a in zhishu:
        for b in zhishu_r:
            if a + b == x:
                print('{} + {} = {} is True !'.format(a,b,x))
                #
                return True
                break

for x in list_main:
    if yanzheng(x):
        list_comp.append(x)

print(list_comp)
# list_comp=list(set(list_comp))
print("is that all true? ",list_comp==list_main)



