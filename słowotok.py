#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

import random

#my_array = array('i', [1,2,3,4,5])

#for i in my_array:
#    print(i)

def slowo(X,Y,tab):
    return (tab[Y[0]][X[0]]+matrix[Y[1]][X[1]]+matrix[Y[2]][X[2]])


#%% Collect letters from polish language
chr_n=[211, 260, 262, 280, 321, 323, 346, 377, 379]
for i in range (65,91):
    chr_n.append(i)

for i in chr_n:    
    print(chr(i))
    
#%% Generate artificial letter matrix
matrix=[[chr(chr_n[random.randint(0, 35)]) for i in range(4)] for j in range(4)]

for i in matrix:
    print(i)

#%% Fins all possible words in matrix

for i in matrix:
    print(i)

slowa=[]

# 3 letters word
x0=0
y0=0

for x0 in range(4):
    for y0 in range(4):
        for i in range(3):
                for j in range(3):
                    for ii in range(3):
                        for jj in range(3):
                            if ((x0>=0) & (y0>=0) & ((x0+i-1)>=0) & ((y0+j-1)>=0) & ((x0+i+ii-2)>=0) & ((y0+j+jj-2)>=0) & \
                                (not ((x0==(x0+i-1)) & (y0==(y0+j-1)))) & \
                                (not (((x0+i-1)==(x0+i+ii-2)) & ((y0+j-1)==(y0+j+jj-2)))) & \
                                (not ((x0==(x0+i+ii-2)) & (y0==(y0+j+jj-2)))) \
                                ):
                                x=[x0,x0+i-1,x0+i+ii-2]
                                y=[y0,y0+j-1,y0+j+jj-2]
                                #print(x,y)
                                try:
                                    slowa.append(slowo(x,y,matrix))
                                except Exception:
                                    pass



print(slowa)
