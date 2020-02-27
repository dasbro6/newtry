
'''
题目：斐波那契数列。
'''

list_fs=[1,1]
print(list_fs[1])
for i in range(100):
    newnum=list_fs[len(list_fs)-1]+list_fs[len(list_fs)-2]

    list_fs.append(newnum)

print(list_fs)
