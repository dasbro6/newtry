'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# '''
new1=1
new2=0
old=0

for i in range(1,20):

    num = old + new1 + new2
    old = old + new2
    new2 = new1
    new1 = old


    print(i,num,"\n")
    # print(i,new1,new2,old)

# f1, f2 = 1, 1
# for i in range(1, 22):
#     # print('%12ld %12ld' % (f1, f2), end='')
#     print(f1,f2)
#     if (i % 3) == 0:
#         print()
#     f1 = f1 + f2
#     f2 = f1 + f2

# x=0
# x_1=1
# x_2=1
# print("第 1 个月 ",1)
# print("第 2 个月 ",1)
# for i in range(30):
#     x=x_1+x_2
#     x_2=x_1
#     x_1=x
#     print("第",str(i+3),"个月 ",x)