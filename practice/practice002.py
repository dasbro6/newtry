'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成；
从键盘输入当月利润I，求应发放奖金总数？
'''


# arr=[0,10,20,40,60,100]
# lv=[0.1,0.075,0.05,0.03,0.015,0.1]
#
# # #shouru=float(input("enter your shouru:"))
#
# def ceshi(shouru):
#     sa=0
#
#     for i in range(1,len(arr)):
#         if shouru>arr[i]:
#             sa+=(arr[i]-arr[i-1])*lv[i-1]
#         else:
#             sa+=(shouru-arr[i-1])*lv[i-1]
#             break
#     print(sa)
#
# ceshilist=[11,21,31,41,51,61,71,81,91,101]
#
# for i in ceshilist:
#     ceshi(i)

arr = (0, 10, 20, 40, 60, 100)
rat = (0, 10, 7.5, 5, 3, 1.5, 1)

def xiti(pro):
    fit=0
    for i in range(1, len(arr)):
        if (pro > arr[i]):
            fit += (arr[i] - arr[i - 1]) * (rat[i] / 100)
        else:
            fit += (pro - arr[i - 1]) * (rat[i] / 100)
            break

    print("奖金（元):",fit)

ceshilist=[11,21,31,41,51,61,71,81,91,101]
for i in ceshilist:
    xiti(i)