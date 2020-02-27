'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''


x=int(input("X："))
y=int(input("Y："))
z=int(input("Z："))

list_a=[x,y,z]
# list_a=[12232,324,435,465,578,689,76896,8,9789,89,3,454,56,5678,678,678,678,6324,545,65,878,9]
list_b=[]
for i in range(len(list_a)):
    maxnum=max(list_a)
    list_b.append(maxnum)
    list_a.remove(maxnum)

print("结果：\n"+str(list_b))