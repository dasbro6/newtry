'''
题目：输出 9*9 乘法口诀表。
'''

for a in range(1,10):

    for b in range(1,a+1):
        exp=("{} * {} = {}".format(str(a),str(b),str(a*b)))
        print(exp, end='\t')
        # \n
        # 换行
        # \v
        # 纵向制表符
        # \t
        # 横向制表符
