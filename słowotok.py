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
TX=[]
TY=[]

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
                                TX.append(x)
                                TY.append(y)
                            except Exception:
                                pass

# 4 letters word - new

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
                                        TX.append(x)
                                        TY.append(y)
                                    except Exception:
                                        pass

# 5 letters word - new

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
                                                TX.append(x)
                                                TY.append(y)                                                         
                                            except Exception:
                                                pass

# 6 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                x1=x0+i1-1
                                                y1=y0+j1-1
                                                x2=x1+i2-1
                                                y2=y1+j2-1
                                                x3=x2+i3-1
                                                y3=y2+j3-1
                                                x4=x3+i4-1
                                                y4=y3+j4-1
                                                x5=x4+i5-1
                                                y5=y4+j5-1
                                                if ((x0>=0) & (y0>=0) & \
                                                    (x1>=0) & (y1>=0) & \
                                                    (x2>=0) & (y2>=0) & \
                                                    (x3>=0) & (y3>=0) & \
                                                    (x4>=0) & (y4>=0) & \
                                                    (x5>=0) & (y5>=0) & \
                                                    (not ((x0==x1) & (y0==y1))) & \
                                                    (not ((x0==x2) & (y0==y2))) & \
                                                    (not ((x0==x3) & (y0==y3))) & \
                                                    (not ((x0==x4) & (y0==y4))) & \
                                                    (not ((x0==x5) & (y0==y5))) & \
                                                    (not ((x1==x2) & (y1==y2))) & \
                                                    (not ((x1==x3) & (y1==y3))) & \
                                                    (not ((x1==x4) & (y1==y4))) & \
                                                    (not ((x1==x5) & (y1==y5))) & \
                                                    (not ((x2==x3) & (y2==y3))) & \
                                                    (not ((x2==x4) & (y2==y4))) & \
                                                    (not ((x2==x5) & (y2==y5))) & \
                                                    (not ((x3==x4) & (y3==y4))) & \
                                                    (not ((x3==x5) & (y3==y5))) & \
                                                    (not ((x4==x5) & (y4==y5))) \
                                                    ):
                                                    x=[x0,x1,x2,x3,x4,x5]
                                                    y=[y0,y1,y2,y3,y4,y5]
                                                    #print(x,y)
                                                    try:
                                                        slowa.append(slowo(x,y,matrix,6))
                                                        TX.append(x)
                                                        TY.append(y)
                                                    except Exception:
                                                        pass

# 7 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                for i6 in range(3):
                                                    for j6 in range(3):
                                                        x1=x0+i1-1
                                                        y1=y0+j1-1
                                                        x2=x1+i2-1
                                                        y2=y1+j2-1
                                                        x3=x2+i3-1
                                                        y3=y2+j3-1
                                                        x4=x3+i4-1
                                                        y4=y3+j4-1
                                                        x5=x4+i5-1
                                                        y5=y4+j5-1
                                                        x6=x5+i6-1
                                                        y6=y5+j6-1
                                                        if ((x0>=0) & (y0>=0) & \
                                                            (x1>=0) & (y1>=0) & \
                                                            (x2>=0) & (y2>=0) & \
                                                            (x3>=0) & (y3>=0) & \
                                                            (x4>=0) & (y4>=0) & \
                                                            (x5>=0) & (y5>=0) & \
                                                            (x6>=0) & (y6>=0) & \
                                                            (not ((x0==x1) & (y0==y1))) & \
                                                            (not ((x0==x2) & (y0==y2))) & \
                                                            (not ((x0==x3) & (y0==y3))) & \
                                                            (not ((x0==x4) & (y0==y4))) & \
                                                            (not ((x0==x5) & (y0==y5))) & \
                                                            (not ((x0==x6) & (y0==y6))) & \
                                                            (not ((x1==x2) & (y1==y2))) & \
                                                            (not ((x1==x3) & (y1==y3))) & \
                                                            (not ((x1==x4) & (y1==y4))) & \
                                                            (not ((x1==x5) & (y1==y5))) & \
                                                            (not ((x1==x6) & (y1==y6))) & \
                                                            (not ((x2==x3) & (y2==y3))) & \
                                                            (not ((x2==x4) & (y2==y4))) & \
                                                            (not ((x2==x5) & (y2==y5))) & \
                                                            (not ((x2==x6) & (y2==y6))) & \
                                                            (not ((x3==x4) & (y3==y4))) & \
                                                            (not ((x3==x5) & (y3==y5))) & \
                                                            (not ((x3==x6) & (y3==y6))) & \
                                                            (not ((x4==x5) & (y4==y5))) & \
                                                            (not ((x4==x6) & (y4==y6))) & \
                                                            (not ((x5==x6) & (y5==y6))) \
                                                            ):
                                                            x=[x0,x1,x2,x3,x4,x5,x6]
                                                            y=[y0,y1,y2,y3,y4,y5,y6]
                                                            #print(x,y)
                                                            try:
                                                                slowa.append(slowo(x,y,matrix,7))
                                                                TX.append(x)
                                                                TY.append(y)
                                                            except Exception:
                                                                pass

# 8 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                for i6 in range(3):
                                                    for j6 in range(3):
                                                        for i7 in range(3):
                                                            for j7 in range(3):
                                                                x1=x0+i1-1
                                                                y1=y0+j1-1
                                                                x2=x1+i2-1
                                                                y2=y1+j2-1
                                                                x3=x2+i3-1
                                                                y3=y2+j3-1
                                                                x4=x3+i4-1
                                                                y4=y3+j4-1
                                                                x5=x4+i5-1
                                                                y5=y4+j5-1
                                                                x6=x5+i6-1
                                                                y6=y5+j6-1
                                                                x7=x6+i7-1
                                                                y7=y6+j7-1
                                                                if ((x0>=0) & (y0>=0) & \
                                                                    (x1>=0) & (y1>=0) & \
                                                                    (x2>=0) & (y2>=0) & \
                                                                    (x3>=0) & (y3>=0) & \
                                                                    (x4>=0) & (y4>=0) & \
                                                                    (x5>=0) & (y5>=0) & \
                                                                    (x6>=0) & (y6>=0) & \
                                                                    (x7>=0) & (y7>=0) & \
                                                                    (not ((x0==x1) & (y0==y1))) & \
                                                                    (not ((x0==x2) & (y0==y2))) & \
                                                                    (not ((x0==x3) & (y0==y3))) & \
                                                                    (not ((x0==x4) & (y0==y4))) & \
                                                                    (not ((x0==x5) & (y0==y5))) & \
                                                                    (not ((x0==x6) & (y0==y6))) & \
                                                                    (not ((x0==x7) & (y0==y7))) & \
                                                                    (not ((x1==x2) & (y1==y2))) & \
                                                                    (not ((x1==x3) & (y1==y3))) & \
                                                                    (not ((x1==x4) & (y1==y4))) & \
                                                                    (not ((x1==x5) & (y1==y5))) & \
                                                                    (not ((x1==x6) & (y1==y6))) & \
                                                                    (not ((x1==x7) & (y1==y7))) & \
                                                                    (not ((x2==x3) & (y2==y3))) & \
                                                                    (not ((x2==x4) & (y2==y4))) & \
                                                                    (not ((x2==x5) & (y2==y5))) & \
                                                                    (not ((x2==x6) & (y2==y6))) & \
                                                                    (not ((x2==x7) & (y2==y7))) & \
                                                                    (not ((x3==x4) & (y3==y4))) & \
                                                                    (not ((x3==x5) & (y3==y5))) & \
                                                                    (not ((x3==x6) & (y3==y6))) & \
                                                                    (not ((x3==x7) & (y3==y7))) & \
                                                                    (not ((x4==x5) & (y4==y5))) & \
                                                                    (not ((x4==x6) & (y4==y6))) & \
                                                                    (not ((x4==x7) & (y4==y7))) & \
                                                                    (not ((x5==x6) & (y5==y6))) & \
                                                                    (not ((x5==x7) & (y5==y7))) & \
                                                                    (not ((x6==x7) & (y6==y7))) \
                                                                    ):
                                                                    x=[x0,x1,x2,x3,x4,x5,x6,x7]
                                                                    y=[y0,y1,y2,y3,y4,y5,y6,y7]
                                                                    #print(x,y)
                                                                    try:
                                                                        slowa.append(slowo(x,y,matrix,8))
                                                                        TX.append(x)
                                                                        TY.append(y)
                                                                    except Exception:
                                                                        pass

# 9 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                for i6 in range(3):
                                                    for j6 in range(3):
                                                        for i7 in range(3):
                                                            for j7 in range(3):
                                                                for i8 in range(3):
                                                                    for j8 in range(3):
                                                                        x1=x0+i1-1
                                                                        y1=y0+j1-1
                                                                        x2=x1+i2-1
                                                                        y2=y1+j2-1
                                                                        x3=x2+i3-1
                                                                        y3=y2+j3-1
                                                                        x4=x3+i4-1
                                                                        y4=y3+j4-1
                                                                        x5=x4+i5-1
                                                                        y5=y4+j5-1
                                                                        x6=x5+i6-1
                                                                        y6=y5+j6-1
                                                                        x7=x6+i7-1
                                                                        y7=y6+j7-1
                                                                        x8=x7+i8-1
                                                                        y8=y7+j8-1
                                                                        if ((x0>=0) & (y0>=0) & \
                                                                            (x1>=0) & (y1>=0) & \
                                                                            (x2>=0) & (y2>=0) & \
                                                                            (x3>=0) & (y3>=0) & \
                                                                            (x4>=0) & (y4>=0) & \
                                                                            (x5>=0) & (y5>=0) & \
                                                                            (x6>=0) & (y6>=0) & \
                                                                            (x7>=0) & (y7>=0) & \
                                                                            (x8>=0) & (y8>=0) & \
                                                                            (not ((x0==x1) & (y0==y1))) & \
                                                                            (not ((x0==x2) & (y0==y2))) & \
                                                                            (not ((x0==x3) & (y0==y3))) & \
                                                                            (not ((x0==x4) & (y0==y4))) & \
                                                                            (not ((x0==x5) & (y0==y5))) & \
                                                                            (not ((x0==x6) & (y0==y6))) & \
                                                                            (not ((x0==x7) & (y0==y7))) & \
                                                                            (not ((x0==x8) & (y0==y8))) & \
                                                                            (not ((x1==x2) & (y1==y2))) & \
                                                                            (not ((x1==x3) & (y1==y3))) & \
                                                                            (not ((x1==x4) & (y1==y4))) & \
                                                                            (not ((x1==x5) & (y1==y5))) & \
                                                                            (not ((x1==x6) & (y1==y6))) & \
                                                                            (not ((x1==x7) & (y1==y7))) & \
                                                                            (not ((x1==x8) & (y1==y8))) & \
                                                                            (not ((x2==x3) & (y2==y3))) & \
                                                                            (not ((x2==x4) & (y2==y4))) & \
                                                                            (not ((x2==x5) & (y2==y5))) & \
                                                                            (not ((x2==x6) & (y2==y6))) & \
                                                                            (not ((x2==x7) & (y2==y7))) & \
                                                                            (not ((x2==x8) & (y2==y8))) & \
                                                                            (not ((x3==x4) & (y3==y4))) & \
                                                                            (not ((x3==x5) & (y3==y5))) & \
                                                                            (not ((x3==x6) & (y3==y6))) & \
                                                                            (not ((x3==x7) & (y3==y7))) & \
                                                                            (not ((x3==x8) & (y3==y8))) & \
                                                                            (not ((x4==x5) & (y4==y5))) & \
                                                                            (not ((x4==x6) & (y4==y6))) & \
                                                                            (not ((x4==x7) & (y4==y7))) & \
                                                                            (not ((x4==x8) & (y4==y8))) & \
                                                                            (not ((x5==x6) & (y5==y6))) & \
                                                                            (not ((x5==x7) & (y5==y7))) & \
                                                                            (not ((x5==x8) & (y5==y8))) & \
                                                                            (not ((x6==x7) & (y6==y7))) & \
                                                                            (not ((x6==x8) & (y6==y8))) & \
                                                                            (not ((x7==x8) & (y7==y8))) \
                                                                            ):
                                                                            x=[x0,x1,x2,x3,x4,x5,x6,x7,x8]
                                                                            y=[y0,y1,y2,y3,y4,y5,y6,y7,y8]
                                                                            #print(x,y)
                                                                            try:
                                                                                slowa.append(slowo(x,y,matrix,9))
                                                                                TX.append(x)
                                                                                TY.append(y)
                                                                            except Exception:
                                                                                pass

# 10 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                for i6 in range(3):
                                                    for j6 in range(3):
                                                        for i7 in range(3):
                                                            for j7 in range(3):
                                                                for i8 in range(3):
                                                                    for j8 in range(3):
                                                                        for i9 in range(3):
                                                                            for j9 in range(3):                                                                        
                                                                                x1=x0+i1-1
                                                                                y1=y0+j1-1
                                                                                x2=x1+i2-1
                                                                                y2=y1+j2-1
                                                                                x3=x2+i3-1
                                                                                y3=y2+j3-1
                                                                                x4=x3+i4-1
                                                                                y4=y3+j4-1
                                                                                x5=x4+i5-1
                                                                                y5=y4+j5-1
                                                                                x6=x5+i6-1
                                                                                y6=y5+j6-1
                                                                                x7=x6+i7-1
                                                                                y7=y6+j7-1
                                                                                x8=x7+i8-1
                                                                                y8=y7+j8-1
                                                                                x9=x8+i9-1
                                                                                y9=y8+j8-1
                                                                                if ((x0>=0) & (y0>=0) & \
                                                                                    (x1>=0) & (y1>=0) & \
                                                                                    (x2>=0) & (y2>=0) & \
                                                                                    (x3>=0) & (y3>=0) & \
                                                                                    (x4>=0) & (y4>=0) & \
                                                                                    (x5>=0) & (y5>=0) & \
                                                                                    (x6>=0) & (y6>=0) & \
                                                                                    (x7>=0) & (y7>=0) & \
                                                                                    (x8>=0) & (y8>=0) & \
                                                                                    (x9>=0) & (y9>=0) & \
                                                                                    (not ((x0==x1) & (y0==y1))) & \
                                                                                    (not ((x0==x2) & (y0==y2))) & \
                                                                                    (not ((x0==x3) & (y0==y3))) & \
                                                                                    (not ((x0==x4) & (y0==y4))) & \
                                                                                    (not ((x0==x5) & (y0==y5))) & \
                                                                                    (not ((x0==x6) & (y0==y6))) & \
                                                                                    (not ((x0==x7) & (y0==y7))) & \
                                                                                    (not ((x0==x8) & (y0==y8))) & \
                                                                                    (not ((x0==x9) & (y0==y9))) & \
                                                                                    (not ((x1==x2) & (y1==y2))) & \
                                                                                    (not ((x1==x3) & (y1==y3))) & \
                                                                                    (not ((x1==x4) & (y1==y4))) & \
                                                                                    (not ((x1==x5) & (y1==y5))) & \
                                                                                    (not ((x1==x6) & (y1==y6))) & \
                                                                                    (not ((x1==x7) & (y1==y7))) & \
                                                                                    (not ((x1==x8) & (y1==y8))) & \
                                                                                    (not ((x1==x9) & (y1==y9))) & \
                                                                                    (not ((x2==x3) & (y2==y3))) & \
                                                                                    (not ((x2==x4) & (y2==y4))) & \
                                                                                    (not ((x2==x5) & (y2==y5))) & \
                                                                                    (not ((x2==x6) & (y2==y6))) & \
                                                                                    (not ((x2==x7) & (y2==y7))) & \
                                                                                    (not ((x2==x8) & (y2==y8))) & \
                                                                                    (not ((x2==x9) & (y2==y9))) & \
                                                                                    (not ((x3==x4) & (y3==y4))) & \
                                                                                    (not ((x3==x5) & (y3==y5))) & \
                                                                                    (not ((x3==x6) & (y3==y6))) & \
                                                                                    (not ((x3==x7) & (y3==y7))) & \
                                                                                    (not ((x3==x8) & (y3==y8))) & \
                                                                                    (not ((x3==x9) & (y3==y9))) & \
                                                                                    (not ((x4==x5) & (y4==y5))) & \
                                                                                    (not ((x4==x6) & (y4==y6))) & \
                                                                                    (not ((x4==x7) & (y4==y7))) & \
                                                                                    (not ((x4==x8) & (y4==y8))) & \
                                                                                    (not ((x4==x9) & (y4==y9))) & \
                                                                                    (not ((x5==x6) & (y5==y6))) & \
                                                                                    (not ((x5==x7) & (y5==y7))) & \
                                                                                    (not ((x5==x8) & (y5==y8))) & \
                                                                                    (not ((x5==x9) & (y5==y9))) & \
                                                                                    (not ((x6==x7) & (y6==y7))) & \
                                                                                    (not ((x6==x8) & (y6==y8))) & \
                                                                                    (not ((x6==x9) & (y6==y9))) & \
                                                                                    (not ((x7==x8) & (y7==y8))) & \
                                                                                    (not ((x7==x9) & (y7==y9))) & \
                                                                                    (not ((x8==x9) & (y8==y9))) \
                                                                                    ):
                                                                                    x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
                                                                                    y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9]
                                                                                    #print(x,y)
                                                                                    try:
                                                                                        slowa.append(slowo(x,y,matrix,10))
                                                                                        TX.append(x)
                                                                                        TY.append(y)
                                                                                    except Exception:
                                                                                        pass

# 11 letters word - new

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
                                        for i5 in range(3):
                                            for j5 in range(3):
                                                for i6 in range(3):
                                                    for j6 in range(3):
                                                        for i7 in range(3):
                                                            for j7 in range(3):
                                                                for i8 in range(3):
                                                                    for j8 in range(3):
                                                                        for i9 in range(3):
                                                                            for j9 in range(3):
                                                                                for i10 in range(3):
                                                                                    for j10 in range(3):
                                                                                        x1=x0+i1-1
                                                                                        y1=y0+j1-1
                                                                                        x2=x1+i2-1
                                                                                        y2=y1+j2-1
                                                                                        x3=x2+i3-1
                                                                                        y3=y2+j3-1
                                                                                        x4=x3+i4-1
                                                                                        y4=y3+j4-1
                                                                                        x5=x4+i5-1
                                                                                        y5=y4+j5-1
                                                                                        x6=x5+i6-1
                                                                                        y6=y5+j6-1
                                                                                        x7=x6+i7-1
                                                                                        y7=y6+j7-1
                                                                                        x8=x7+i8-1
                                                                                        y8=y7+j8-1
                                                                                        x9=x8+i9-1
                                                                                        y9=y8+j9-1
                                                                                        x10=x9+i10-1
                                                                                        y10=y9+j10-1
                                                                                        if ((x0>=0) & (y0>=0) & \
                                                                                            (x1>=0) & (y1>=0) & \
                                                                                            (x2>=0) & (y2>=0) & \
                                                                                            (x3>=0) & (y3>=0) & \
                                                                                            (x4>=0) & (y4>=0) & \
                                                                                            (x5>=0) & (y5>=0) & \
                                                                                            (x6>=0) & (y6>=0) & \
                                                                                            (x7>=0) & (y7>=0) & \
                                                                                            (x8>=0) & (y8>=0) & \
                                                                                            (x9>=0) & (y9>=0) & \
                                                                                            (x10>=0) & (y10>=0) & \
                                                                                            (not ((x0==x1) & (y0==y1))) & \
                                                                                            (not ((x0==x2) & (y0==y2))) & \
                                                                                            (not ((x0==x3) & (y0==y3))) & \
                                                                                            (not ((x0==x4) & (y0==y4))) & \
                                                                                            (not ((x0==x5) & (y0==y5))) & \
                                                                                            (not ((x0==x6) & (y0==y6))) & \
                                                                                            (not ((x0==x7) & (y0==y7))) & \
                                                                                            (not ((x0==x8) & (y0==y8))) & \
                                                                                            (not ((x0==x9) & (y0==y9))) & \
                                                                                            (not ((x0==x10) & (y0==y10))) & \
                                                                                            (not ((x1==x2) & (y1==y2))) & \
                                                                                            (not ((x1==x3) & (y1==y3))) & \
                                                                                            (not ((x1==x4) & (y1==y4))) & \
                                                                                            (not ((x1==x5) & (y1==y5))) & \
                                                                                            (not ((x1==x6) & (y1==y6))) & \
                                                                                            (not ((x1==x7) & (y1==y7))) & \
                                                                                            (not ((x1==x8) & (y1==y8))) & \
                                                                                            (not ((x1==x9) & (y1==y9))) & \
                                                                                            (not ((x1==x10) & (y1==y10))) & \
                                                                                            (not ((x2==x3) & (y2==y3))) & \
                                                                                            (not ((x2==x4) & (y2==y4))) & \
                                                                                            (not ((x2==x5) & (y2==y5))) & \
                                                                                            (not ((x2==x6) & (y2==y6))) & \
                                                                                            (not ((x2==x7) & (y2==y7))) & \
                                                                                            (not ((x2==x8) & (y2==y8))) & \
                                                                                            (not ((x2==x9) & (y2==y9))) & \
                                                                                            (not ((x2==x10) & (y2==y10))) & \
                                                                                            (not ((x3==x4) & (y3==y4))) & \
                                                                                            (not ((x3==x5) & (y3==y5))) & \
                                                                                            (not ((x3==x6) & (y3==y6))) & \
                                                                                            (not ((x3==x7) & (y3==y7))) & \
                                                                                            (not ((x3==x8) & (y3==y8))) & \
                                                                                            (not ((x3==x9) & (y3==y9))) & \
                                                                                            (not ((x3==x10) & (y3==y10))) & \
                                                                                            (not ((x4==x5) & (y4==y5))) & \
                                                                                            (not ((x4==x6) & (y4==y6))) & \
                                                                                            (not ((x4==x7) & (y4==y7))) & \
                                                                                            (not ((x4==x8) & (y4==y8))) & \
                                                                                            (not ((x4==x9) & (y4==y9))) & \
                                                                                            (not ((x4==x10) & (y4==y10))) & \
                                                                                            (not ((x5==x6) & (y5==y6))) & \
                                                                                            (not ((x5==x7) & (y5==y7))) & \
                                                                                            (not ((x5==x8) & (y5==y8))) & \
                                                                                            (not ((x5==x9) & (y5==y9))) & \
                                                                                            (not ((x5==x10) & (y5==y10))) & \
                                                                                            (not ((x6==x7) & (y6==y7))) & \
                                                                                            (not ((x6==x8) & (y6==y8))) & \
                                                                                            (not ((x6==x9) & (y6==y9))) & \
                                                                                            (not ((x6==x10) & (y6==y10))) & \
                                                                                            (not ((x7==x8) & (y7==y8))) & \
                                                                                            (not ((x7==x9) & (y7==y9))) & \
                                                                                            (not ((x7==x10) & (y7==y10))) & \
                                                                                            (not ((x8==x9) & (y8==y9))) & \
                                                                                            (not ((x8==x10) & (y8==y10))) & \
                                                                                            (not ((x9==x10) & (y9==y10))) \
                                                                                            ):
                                                                                            x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
                                                                                            y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
                                                                                            #print(x,y)
                                                                                            try:
                                                                                                slowa.append(slowo(x,y,matrix,11))
                                                                                                TX.append(x)
                                                                                                TY.append(y)
                                                                                            except Exception:
                                                                                                pass

#print(slowa)
#for ll in matrix:
#    print(ll)
                                                                        
print(len(TX))
