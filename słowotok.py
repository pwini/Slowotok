#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

import random

#my_array = array('i', [1,2,3,4,5])

#for i in my_array:
#    print(i)

def slowo(X,Y,tab,n):
    sl=''
    for i in range(n):
        sl=sl+tab[X[i]][Y[i]]
    return sl
'''
def slowo3(X,Y,tab):
    return (tab[Y[0]][X[0]]+tab[Y[1]][X[1]]+tab[Y[2]][X[2]])

def slowo4(X,Y,tab):
    return (tab[Y[0]][X[0]]+tab[Y[1]][X[1]]+tab[Y[2]][X[2]]+tab[Y[3]][X[3]])
'''

#%% Collect letters from polish language
chr_n=[211, 260, 262, 280, 321, 323, 346, 377, 379]
for i in range (65,91):
    chr_n.append(i)

#for i in chr_n:    
#    print(chr(i))
    
#%% Generate artificial letter matrix
matrix=[[chr(chr_n[random.randint(0, 34)]) for i in range(4)] for j in range(4)]

#for i in matrix:
#    print(i)

#%% Fins all possible words in matrix

#for i in matrix:
#    print(i)

slowa=[]

'''
# 3 letters word - old
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
'''

# 3 letters word - new
x0=0
y0=0

for x0 in range(4):
    for y0 in range(4):
        for i1 in range(3):
            for j1 in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        x1=x0+i1-1
                        y1=y0+i1-1
                        x2=x1+i2-1
                        y2=y1+j2-1
                        if ((x0>=0) & (y0>=0) & (x1>=0) & (y1>=0) & (x2>=0) & (y2>=0)) & \
                            (not ((x0==(x1) & (y0==y1))) & \
                            (not ((x1==x2) & (y1==y2))) & \
                            (not ((x0==x2) & (y0==y2))) \
                            ):
                            x=[x0,x1,x2]
                            y=[y0,y1,y2]
                            #print(x,y)
                            try:
                                slowa.append(slowo(x,y,matrix,3))
                            except Exception:
                                pass

# 4 letters word - new
x0=0
y0=0

for x0 in range(4):
    for y0 in range(4):
        for i1 in range(3):
            for j1 in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        for i3 in range(3):
                            for j3 in range(3):
                                x1=x0+i1-1
                                y1=y0+i1-1
                                x2=x1+i2-1
                                y2=y1+j2-1
                                x3=x2+i3-1
                                y3=y2+j3-1
                                if ((x0>=0) & (y0>=0) & \
                                    (x1>=0) & (y1>=0) & \
                                    (x2>=0) & (y2>=0) & \
                                    (x3>=0) & (y3>=0) & \
                                    (not ((x0==x1) & (y0==y1))) & \
                                    (not ((x0==x2) & (y0==y2))) & \
                                    (not ((x0==x3) & (y0==y3))) & \
                                    (not ((x1==x2) & (y1==y2))) & \
                                    (not ((x1==x3) & (y1==y3))) & \
                                    (not ((x2==x3) & (y2==y3))) \
                                    ):
                                    x=[x0,x1,x2,x3]
                                    y=[y0,y1,y2,y3]
                                    #print(x,y)
                                    try:
                                        slowa.append(slowo(x,y,matrix,4))
                                    except Exception:
                                        pass

for x0 in range(4):
    for y0 in range(4):
        for i1 in range(3):
            for j1 in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        for i3 in range(3):
                            for j3 in range(3):
                                for i4 in range(3):
                                    for j4 in range(3):
                                        x1=x0+i1-1
                                        y1=y0+i1-1
                                        x2=x1+i2-1
                                        y2=y1+j2-1
                                        x3=x2+i3-1
                                        y3=y2+j3-1
                                        x4=x3+i4-1
                                        y4=y3+j4-1
                                        if ((x0>=0) & (y0>=0) & \
                                            (x1>=0) & (y1>=0) & \
                                            (x2>=0) & (y2>=0) & \
                                            (x3>=0) & (y3>=0) & \
                                            (x4>=0) & (y4>=0) & \
                                            (not ((x0==x1) & (y0==y1))) & \
                                            (not ((x0==x2) & (y0==y2))) & \
                                            (not ((x0==x3) & (y0==y3))) & \
                                            (not ((x0==x4) & (y0==y4))) & \
                                            (not ((x1==x2) & (y1==y2))) & \
                                            (not ((x1==x3) & (y1==y3))) & \
                                            (not ((x1==x4) & (y1==y4))) & \
                                            (not ((x2==x3) & (y2==y3))) & \
                                            (not ((x2==x4) & (y2==y4))) & \
                                            (not ((x3==x4) & (y3==y4))) \
                                            ):
                                            x=[x0,x1,x2,x3,x4]
                                            y=[y0,y1,y2,y3,y4]
                                            #print(x,y)
                                            try:
                                                slowa.append(slowo(x,y,matrix,5))
                                            except Exception:
                                                pass

print(slowa)
for ll in matrix:
    print(ll)
