'''
题目：格式化输出当前时间。
'''

import time


local = time.localtime()

print(time.strftime('%Y-%m-%d',local))



# import time
#
# format = '%Y-%m-%d %H:%M:%S'
# local = time.localtime(time.time())
#
# print(time.strftime(format,local))