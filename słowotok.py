#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

import array
import random

def matryca(dim):
    matrix=[[(j*dim)+(i+1) for i in range(dim)] for j in range(dim)]

    #print(matrix)
    #for i in range(dim):
    #    for j in range(dim):
    #        print(matrix[i][j])


def trzy_litery():
    dim=3
    tablica=[]
    tablica=[[(j*dim)+(i+1) for i in range(dim)] for j in range(dim)]
    print(tablica)
 
    x1=0
    y1=0
    licznik=1
    while x1<3 and x1>-1:
        while y1<3 and y1>-1:
            for x2 in range(2):
                for y2 in range(2):
                    for x3 in range(2):
                        for y3 in range(2):
                            if x1+x2+x3<3 and y1+y2+y3<3:
                                #print(matryca([x1][y1]))
                                #litera_1.append(a1)
                                #a2=matryca([x2][y2])
                                #litera_2.append(a2)
                                #a3=matryca([x3][y3])
                                #litera_3.append(a3)
                                #print('x3= ', x3)
                                #print('y3= ', y3)
                                #licznik=licznik+1
                                print('licznik =' , licznik)
                                licznik=licznik+1
                                if licznik>100:
                                    print('Przerywamy...')
                                    break
            y1=y1+1
        x1=x1+1
    print(tablica)
                    


