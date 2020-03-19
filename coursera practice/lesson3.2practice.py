# # -*- coding: utf-8 -*-
# """
# create DataFrame object
# """
# import pandas as pd
# music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
#
# music_table = pd.DataFrame(music_data)
# music_table.index = range(1,5)
# music_table.columns = ['singer','song_name']
# print(music_table)

import numpy as np
from math import sqrt
import time

#Numpy通用函数
start_np = time.time()
arr = np.arange(1000000)
print(np.sqrt(arr))
stop_np = time.time()

# Math库函数
start_math = time.time()
list =[]
for i in range(1000000):
    list.append(sqrt(i))
print(list)
stop_math = time.time()
print('Numpy通用函数用时{}，Math函数用时{}'.format(stop_np-start_np,stop_math-start_math))