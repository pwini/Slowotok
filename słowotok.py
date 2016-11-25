#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

from array import *
import random

#my_array = array('i', [1,2,3,4,5])

#for i in my_array:
#    print(i)


matrix=[[random.randint(1, 10) for i in range(3)] for j in range(3)]
#matrix=random.randint(1, 10)
print(matrix)
for i in range(3):
    for j in range(3):
        print(matrix[i][j])


