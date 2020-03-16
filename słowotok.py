#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

import random
import itertools
import csv

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

# Collect letters from polish language
chr_n=[211, 260, 262, 280, 321, 323, 346, 377, 379]
for i in range (65,91):
    chr_n.append(i)
    
# Generate artificial letter matrix
matrix=[[chr(chr_n[random.randint(0, 34)]) for i in range(4)] for j in range(4)]

# Find all possible words in matrix

#for i in matrix:
#    print(i)

slowa=[]
TX=[]
TY=[]

#
X0=set([0,1,2,3])
Y0=set([0,1,2,3])

xn=set([0,1,2])
yn=set([0,1,2])

#
#for s in slowa:
#    print(s)

#
    
#print(len(slowa))


#%%
'''
print('3 letters word')

for e in itertools.product(X0,Y0,xn,yn,xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
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
'''                            
#%%
print('3 letters word')

for x0 in range(4):
    for y0 in range(4):
        for i1 in range(3):
            for j1 in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        x1=x0+i1-1
                        y1=y0+j1-1
                        x2=x1+i2-1
                        y2=y1+j2-1
                        if (((x0>=0) & (y0>=0) & (x1>=0) & (y1>=0) & (x2>=0) & (y2>=0)) & \
                        ((x0<=3) & (y0<=3) & (x1<=3) & (y1<=3) & (x2<=3) & (y2<=3)) & \
                        (not ((x0==x1) & (y0==y1))) & \
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



#%%

print('4 letters word')

k=2
XK=[]
YK=[]
for xk,yk in zip(TX,TY):
    for i in range(3):
        for j in range(3):
            repeated_item=False
            xk_1=xk[k]+i-1
            yk_1=yk[k]+j-1
            if ((xk_1>=0) & (yk_1>=0) & (xk_1<=3) & (yk_1<=3)):
                for l in range(k+1):
                    if ((xk_1==xk[l]) & (yk_1==yk[l])):
                        repeated_item=True
                        break
                if not repeated_item:
                    x_tmp=xk[:]
                    y_tmp=yk[:]
                    x_tmp.append(xk_1)
                    y_tmp.append(yk_1)
                    XK.append(x_tmp)
                    YK.append(y_tmp)                
                    slowa.append(slowo(x_tmp, y_tmp, matrix,k+2))
                    
#%%

print(len(XK))
print(len(YK))
for i in range(len(XK)):
    print(XK[i],YK[i])
                             
#%%

print('4 letters word')

for e in itertools.product(X0,Y0,xn,yn,xn,yn,xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
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
#%%

print('5 letters word')

for e in itertools.product(X0,Y0,xn,yn,xn,yn,xn,yn,xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
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

#%%

print('6 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn, yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
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

#%%

print('7 letters word')


for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
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

#%%

print('8 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
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

#%%

print('9 letters word')
for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
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

#%%

print('10 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
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
        try:
            slowa.append(slowo(x,y,matrix,10))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass

#%%

print('11 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
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

#%%

print('12 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
    x11=x10+e[22]-1
    y11=y10+e[22]-1
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
        (x11>=0) & (y11>=0) & \
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
        (not ((x0==x11) & (y0==y11))) & \
        (not ((x1==x2) & (y1==y2))) & \
        (not ((x1==x3) & (y1==y3))) & \
        (not ((x1==x4) & (y1==y4))) & \
        (not ((x1==x5) & (y1==y5))) & \
        (not ((x1==x6) & (y1==y6))) & \
        (not ((x1==x7) & (y1==y7))) & \
        (not ((x1==x8) & (y1==y8))) & \
        (not ((x1==x9) & (y1==y9))) & \
        (not ((x1==x10) & (y1==y10))) & \
        (not ((x1==x11) & (y1==y11))) & \
        (not ((x2==x3) & (y2==y3))) & \
        (not ((x2==x4) & (y2==y4))) & \
        (not ((x2==x5) & (y2==y5))) & \
        (not ((x2==x6) & (y2==y6))) & \
        (not ((x2==x7) & (y2==y7))) & \
        (not ((x2==x8) & (y2==y8))) & \
        (not ((x2==x9) & (y2==y9))) & \
        (not ((x2==x10) & (y2==y10))) & \
        (not ((x2==x11) & (y2==y11))) & \
        (not ((x3==x4) & (y3==y4))) & \
        (not ((x3==x5) & (y3==y5))) & \
        (not ((x3==x6) & (y3==y6))) & \
        (not ((x3==x7) & (y3==y7))) & \
        (not ((x3==x8) & (y3==y8))) & \
        (not ((x3==x9) & (y3==y9))) & \
        (not ((x3==x10) & (y3==y10))) & \
        (not ((x3==x11) & (y3==y11))) & \
        (not ((x4==x5) & (y4==y5))) & \
        (not ((x4==x6) & (y4==y6))) & \
        (not ((x4==x7) & (y4==y7))) & \
        (not ((x4==x8) & (y4==y8))) & \
        (not ((x4==x9) & (y4==y9))) & \
        (not ((x4==x10) & (y4==y10))) & \
        (not ((x4==x11) & (y4==y11))) & \
        (not ((x5==x6) & (y5==y6))) & \
        (not ((x5==x7) & (y5==y7))) & \
        (not ((x5==x8) & (y5==y8))) & \
        (not ((x5==x9) & (y5==y9))) & \
        (not ((x5==x10) & (y5==y10))) & \
        (not ((x5==x11) & (y5==y11))) & \
        (not ((x6==x7) & (y6==y7))) & \
        (not ((x6==x8) & (y6==y8))) & \
        (not ((x6==x9) & (y6==y9))) & \
        (not ((x6==x10) & (y6==y10))) & \
        (not ((x6==x11) & (y6==y11))) & \
        (not ((x7==x8) & (y7==y8))) & \
        (not ((x7==x9) & (y7==y9))) & \
        (not ((x7==x10) & (y7==y10))) & \
        (not ((x7==x11) & (y7==y11))) & \
        (not ((x8==x9) & (y8==y9))) & \
        (not ((x8==x10) & (y8==y10))) & \
        (not ((x8==x11) & (y8==y11))) & \
        (not ((x9==x10) & (y9==y10))) & \
        (not ((x9==x11) & (y9==y11))) & \
        (not ((x10==x11) & (y10==y11))) \
        ):
        x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11]
        y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]
        #print(x,y)
        try:
            slowa.append(slowo(x,y,matrix,12))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass

#%%

print('13 letters word')


for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
    x11=x10+e[22]-1
    y11=y10+e[22]-1
    x12=x11+e[23]-1
    y12=y11+e[24]-1
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
        (x11>=0) & (y11>=0) & \
        (x12>=0) & (y12>=0) & \
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
        (not ((x0==x11) & (y0==y11))) & \
        (not ((x0==x12) & (y0==y12))) & \
        (not ((x1==x2) & (y1==y2))) & \
        (not ((x1==x3) & (y1==y3))) & \
        (not ((x1==x4) & (y1==y4))) & \
        (not ((x1==x5) & (y1==y5))) & \
        (not ((x1==x6) & (y1==y6))) & \
        (not ((x1==x7) & (y1==y7))) & \
        (not ((x1==x8) & (y1==y8))) & \
        (not ((x1==x9) & (y1==y9))) & \
        (not ((x1==x10) & (y1==y10))) & \
        (not ((x1==x11) & (y1==y11))) & \
        (not ((x1==x12) & (y1==y12))) & \
        (not ((x2==x3) & (y2==y3))) & \
        (not ((x2==x4) & (y2==y4))) & \
        (not ((x2==x5) & (y2==y5))) & \
        (not ((x2==x6) & (y2==y6))) & \
        (not ((x2==x7) & (y2==y7))) & \
        (not ((x2==x8) & (y2==y8))) & \
        (not ((x2==x9) & (y2==y9))) & \
        (not ((x2==x10) & (y2==y10))) & \
        (not ((x2==x11) & (y2==y11))) & \
        (not ((x2==x12) & (y2==y12))) & \
        (not ((x3==x4) & (y3==y4))) & \
        (not ((x3==x5) & (y3==y5))) & \
        (not ((x3==x6) & (y3==y6))) & \
        (not ((x3==x7) & (y3==y7))) & \
        (not ((x3==x8) & (y3==y8))) & \
        (not ((x3==x9) & (y3==y9))) & \
        (not ((x3==x10) & (y3==y10))) & \
        (not ((x3==x11) & (y3==y11))) & \
        (not ((x3==x12) & (y3==y12))) & \
        (not ((x4==x5) & (y4==y5))) & \
        (not ((x4==x6) & (y4==y6))) & \
        (not ((x4==x7) & (y4==y7))) & \
        (not ((x4==x8) & (y4==y8))) & \
        (not ((x4==x9) & (y4==y9))) & \
        (not ((x4==x10) & (y4==y10))) & \
        (not ((x4==x11) & (y4==y11))) & \
        (not ((x4==x12) & (y4==y12))) & \
        (not ((x5==x6) & (y5==y6))) & \
        (not ((x5==x7) & (y5==y7))) & \
        (not ((x5==x8) & (y5==y8))) & \
        (not ((x5==x9) & (y5==y9))) & \
        (not ((x5==x10) & (y5==y10))) & \
        (not ((x5==x11) & (y5==y11))) & \
        (not ((x5==x12) & (y5==y12))) & \
        (not ((x6==x7) & (y6==y7))) & \
        (not ((x6==x8) & (y6==y8))) & \
        (not ((x6==x9) & (y6==y9))) & \
        (not ((x6==x10) & (y6==y10))) & \
        (not ((x6==x11) & (y6==y11))) & \
        (not ((x6==x12) & (y6==y12))) & \
        (not ((x7==x8) & (y7==y8))) & \
        (not ((x7==x9) & (y7==y9))) & \
        (not ((x7==x10) & (y7==y10))) & \
        (not ((x7==x11) & (y7==y11))) & \
        (not ((x7==x12) & (y7==y12))) & \
        (not ((x8==x9) & (y8==y9))) & \
        (not ((x8==x10) & (y8==y10))) & \
        (not ((x8==x11) & (y8==y11))) & \
        (not ((x8==x12) & (y8==y12))) & \
        (not ((x9==x10) & (y9==y10))) & \
        (not ((x9==x11) & (y9==y11))) & \
        (not ((x9==x12) & (y9==y12))) & \
        (not ((x10==x11) & (y10==y11))) & \
        (not ((x10==x12) & (y10==y12))) & \
        (not ((x11==x12) & (y11==y12))) \
        ):
        x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
        y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]
        #print(x,y)
        try:
            slowa.append(slowo(x,y,matrix,13))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass

#%%

print('14 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
    x11=x10+e[22]-1
    y11=y10+e[23]-1
    x12=x11+e[24]-1
    y12=y11+e[25]-1
    x13=x12+e[26]-1
    y13=y12+e[27]-1
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
        (x11>=0) & (y11>=0) & \
        (x12>=0) & (y12>=0) & \
        (x13>=0) & (y13>=0) & \
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
        (not ((x0==x11) & (y0==y11))) & \
        (not ((x0==x12) & (y0==y12))) & \
        (not ((x0==x13) & (y0==y13))) & \
        (not ((x1==x2) & (y1==y2))) & \
        (not ((x1==x3) & (y1==y3))) & \
        (not ((x1==x4) & (y1==y4))) & \
        (not ((x1==x5) & (y1==y5))) & \
        (not ((x1==x6) & (y1==y6))) & \
        (not ((x1==x7) & (y1==y7))) & \
        (not ((x1==x8) & (y1==y8))) & \
        (not ((x1==x9) & (y1==y9))) & \
        (not ((x1==x10) & (y1==y10))) & \
        (not ((x1==x11) & (y1==y11))) & \
        (not ((x1==x12) & (y1==y12))) & \
        (not ((x1==x13) & (y1==y13))) & \
        (not ((x2==x3) & (y2==y3))) & \
        (not ((x2==x4) & (y2==y4))) & \
        (not ((x2==x5) & (y2==y5))) & \
        (not ((x2==x6) & (y2==y6))) & \
        (not ((x2==x7) & (y2==y7))) & \
        (not ((x2==x8) & (y2==y8))) & \
        (not ((x2==x9) & (y2==y9))) & \
        (not ((x2==x10) & (y2==y10))) & \
        (not ((x2==x11) & (y2==y11))) & \
        (not ((x2==x12) & (y2==y12))) & \
        (not ((x2==x13) & (y2==y13))) & \
        (not ((x3==x4) & (y3==y4))) & \
        (not ((x3==x5) & (y3==y5))) & \
        (not ((x3==x6) & (y3==y6))) & \
        (not ((x3==x7) & (y3==y7))) & \
        (not ((x3==x8) & (y3==y8))) & \
        (not ((x3==x9) & (y3==y9))) & \
        (not ((x3==x10) & (y3==y10))) & \
        (not ((x3==x11) & (y3==y11))) & \
        (not ((x3==x12) & (y3==y12))) & \
        (not ((x3==x13) & (y3==y13))) & \
        (not ((x4==x5) & (y4==y5))) & \
        (not ((x4==x6) & (y4==y6))) & \
        (not ((x4==x7) & (y4==y7))) & \
        (not ((x4==x8) & (y4==y8))) & \
        (not ((x4==x9) & (y4==y9))) & \
        (not ((x4==x10) & (y4==y10))) & \
        (not ((x4==x11) & (y4==y11))) & \
        (not ((x4==x12) & (y4==y12))) & \
        (not ((x4==x13) & (y4==y13))) & \
        (not ((x5==x6) & (y5==y6))) & \
        (not ((x5==x7) & (y5==y7))) & \
        (not ((x5==x8) & (y5==y8))) & \
        (not ((x5==x9) & (y5==y9))) & \
        (not ((x5==x10) & (y5==y10))) & \
        (not ((x5==x11) & (y5==y11))) & \
        (not ((x5==x12) & (y5==y12))) & \
        (not ((x5==x13) & (y5==y13))) & \
        (not ((x6==x7) & (y6==y7))) & \
        (not ((x6==x8) & (y6==y8))) & \
        (not ((x6==x9) & (y6==y9))) & \
        (not ((x6==x10) & (y6==y10))) & \
        (not ((x6==x11) & (y6==y11))) & \
        (not ((x6==x12) & (y6==y12))) & \
        (not ((x6==x13) & (y6==y13))) & \
        (not ((x7==x8) & (y7==y8))) & \
        (not ((x7==x9) & (y7==y9))) & \
        (not ((x7==x10) & (y7==y10))) & \
        (not ((x7==x11) & (y7==y11))) & \
        (not ((x7==x12) & (y7==y12))) & \
        (not ((x7==x13) & (y7==y13))) & \
        (not ((x8==x9) & (y8==y9))) & \
        (not ((x8==x10) & (y8==y10))) & \
        (not ((x8==x11) & (y8==y11))) & \
        (not ((x8==x12) & (y8==y12))) & \
        (not ((x8==x13) & (y8==y13))) & \
        (not ((x9==x10) & (y9==y10))) & \
        (not ((x9==x11) & (y9==y11))) & \
        (not ((x9==x12) & (y9==y12))) & \
        (not ((x9==x13) & (y9==y13))) & \
        (not ((x10==x11) & (y10==y11))) & \
        (not ((x10==x12) & (y10==y12))) & \
        (not ((x10==x13) & (y10==y13))) & \
        (not ((x11==x12) & (y11==y12))) & \
        (not ((x11==x13) & (y11==y13))) & \
        (not ((x12==x13) & (y12==y13))) \
        ):
        x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]
        y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]
        #print(x,y)
        try:
            slowa.append(slowo(x,y,matrix,14))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass

#%%

print('15 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
    x11=x10+e[22]-1
    y11=y10+e[23]-1
    x12=x11+e[24]-1
    y12=y11+e[25]-1
    x13=x12+e[26]-1
    y13=y12+e[27]-1
    x14=x13+e[28]-1
    y14=x14+e[29]-1
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
        (x11>=0) & (y11>=0) & \
        (x12>=0) & (y12>=0) & \
        (x13>=0) & (y13>=0) & \
        (x14>=0) & (y14>=0) & \
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
        (not ((x0==x11) & (y0==y11))) & \
        (not ((x0==x12) & (y0==y12))) & \
        (not ((x0==x13) & (y0==y13))) & \
        (not ((x0==x14) & (y0==y14))) & \
        (not ((x1==x2) & (y1==y2))) & \
        (not ((x1==x3) & (y1==y3))) & \
        (not ((x1==x4) & (y1==y4))) & \
        (not ((x1==x5) & (y1==y5))) & \
        (not ((x1==x6) & (y1==y6))) & \
        (not ((x1==x7) & (y1==y7))) & \
        (not ((x1==x8) & (y1==y8))) & \
        (not ((x1==x9) & (y1==y9))) & \
        (not ((x1==x10) & (y1==y10))) & \
        (not ((x1==x11) & (y1==y11))) & \
        (not ((x1==x12) & (y1==y12))) & \
        (not ((x1==x13) & (y1==y13))) & \
        (not ((x1==x14) & (y1==y14))) & \
        (not ((x2==x3) & (y2==y3))) & \
        (not ((x2==x4) & (y2==y4))) & \
        (not ((x2==x5) & (y2==y5))) & \
        (not ((x2==x6) & (y2==y6))) & \
        (not ((x2==x7) & (y2==y7))) & \
        (not ((x2==x8) & (y2==y8))) & \
        (not ((x2==x9) & (y2==y9))) & \
        (not ((x2==x10) & (y2==y10))) & \
        (not ((x2==x11) & (y2==y11))) & \
        (not ((x2==x12) & (y2==y12))) & \
        (not ((x2==x13) & (y2==y13))) & \
        (not ((x2==x14) & (y2==y14))) & \
        (not ((x3==x4) & (y3==y4))) & \
        (not ((x3==x5) & (y3==y5))) & \
        (not ((x3==x6) & (y3==y6))) & \
        (not ((x3==x7) & (y3==y7))) & \
        (not ((x3==x8) & (y3==y8))) & \
        (not ((x3==x9) & (y3==y9))) & \
        (not ((x3==x10) & (y3==y10))) & \
        (not ((x3==x11) & (y3==y11))) & \
        (not ((x3==x12) & (y3==y12))) & \
        (not ((x3==x13) & (y3==y13))) & \
        (not ((x3==x14) & (y3==y14))) & \
        (not ((x4==x5) & (y4==y5))) & \
        (not ((x4==x6) & (y4==y6))) & \
        (not ((x4==x7) & (y4==y7))) & \
        (not ((x4==x8) & (y4==y8))) & \
        (not ((x4==x9) & (y4==y9))) & \
        (not ((x4==x10) & (y4==y10))) & \
        (not ((x4==x11) & (y4==y11))) & \
        (not ((x4==x12) & (y4==y12))) & \
        (not ((x4==x13) & (y4==y13))) & \
        (not ((x4==x14) & (y4==y14))) & \
        (not ((x5==x6) & (y5==y6))) & \
        (not ((x5==x7) & (y5==y7))) & \
        (not ((x5==x8) & (y5==y8))) & \
        (not ((x5==x9) & (y5==y9))) & \
        (not ((x5==x10) & (y5==y10))) & \
        (not ((x5==x11) & (y5==y11))) & \
        (not ((x5==x12) & (y5==y12))) & \
        (not ((x5==x13) & (y5==y13))) & \
        (not ((x5==x14) & (y5==y14))) & \
        (not ((x6==x7) & (y6==y7))) & \
        (not ((x6==x8) & (y6==y8))) & \
        (not ((x6==x9) & (y6==y9))) & \
        (not ((x6==x10) & (y6==y10))) & \
        (not ((x6==x11) & (y6==y11))) & \
        (not ((x6==x12) & (y6==y12))) & \
        (not ((x6==x13) & (y6==y13))) & \
        (not ((x6==x14) & (y6==y14))) & \
        (not ((x7==x8) & (y7==y8))) & \
        (not ((x7==x9) & (y7==y9))) & \
        (not ((x7==x10) & (y7==y10))) & \
        (not ((x7==x11) & (y7==y11))) & \
        (not ((x7==x12) & (y7==y12))) & \
        (not ((x7==x13) & (y7==y13))) & \
        (not ((x7==x14) & (y7==y14))) & \
        (not ((x8==x9) & (y8==y9))) & \
        (not ((x8==x10) & (y8==y10))) & \
        (not ((x8==x11) & (y8==y11))) & \
        (not ((x8==x12) & (y8==y12))) & \
        (not ((x8==x13) & (y8==y13))) & \
        (not ((x8==x14) & (y8==y14))) & \
        (not ((x9==x10) & (y9==y10))) & \
        (not ((x9==x11) & (y9==y11))) & \
        (not ((x9==x12) & (y9==y12))) & \
        (not ((x9==x13) & (y9==y13))) & \
        (not ((x9==x14) & (y9==y14))) & \
        (not ((x10==x11) & (y10==y11))) & \
        (not ((x10==x12) & (y10==y12))) & \
        (not ((x10==x13) & (y10==y13))) & \
        (not ((x10==x14) & (y10==y14))) & \
        (not ((x11==x12) & (y11==y12))) & \
        (not ((x11==x13) & (y11==y13))) & \
        (not ((x11==x14) & (y11==y14))) & \
        (not ((x12==x13) & (y12==y13))) & \
        (not ((x12==x14) & (y12==y14))) & \
        (not ((x13==x14) & (y13==y14))) \
        ):
        x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14]
        y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]
        #print(x,y)
        try:
            slowa.append(slowo(x,y,matrix,15))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass

#%%

print('16 letters word')

for e in itertools.product(X0,Y0, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn ,xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn, xn,yn):
    x0=e[0]
    y0=e[1]
    x1=x0+e[2]-1
    y1=y0+e[3]-1
    x2=x1+e[4]-1
    y2=y1+e[5]-1
    x3=x2+e[6]-1
    y3=y2+e[7]-1
    x4=x3+e[8]-1
    y4=y3+e[9]-1
    x5=x4+e[10]-1
    y5=y4+e[11]-1
    x6=x5+e[12]-1
    y6=y5+e[13]-1
    x7=x6+e[14]-1
    y7=y6+e[15]-1
    x8=x7+e[16]-1
    y8=y7+e[17]-1
    x9=x8+e[18]-1
    y9=y8+e[19]-1
    x10=x9+e[20]-1
    y10=y9+e[21]-1
    x11=x10+e[22]-1
    y11=y10+e[23]-1
    x12=x11+e[24]-1
    y12=y11+e[25]-1
    x13=x12+e[26]-1
    y13=y12+e[27]-1
    x14=x13+e[28]-1
    y14=x13+e[29]-1
    x15=x14+e[30]-1
    y15=y14+e[31]-1
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
        (x11>=0) & (y11>=0) & \
        (x12>=0) & (y12>=0) & \
        (x13>=0) & (y13>=0) & \
        (x14>=0) & (y14>=0) & \
        (x15>=0) & (y15>=0) & \
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
        (not ((x0==x11) & (y0==y11))) & \
        (not ((x0==x12) & (y0==y12))) & \
        (not ((x0==x13) & (y0==y13))) & \
        (not ((x0==x14) & (y0==y14))) & \
        (not ((x0==x15) & (y0==y15))) & \
        (not ((x1==x2) & (y1==y2))) & \
        (not ((x1==x3) & (y1==y3))) & \
        (not ((x1==x4) & (y1==y4))) & \
        (not ((x1==x5) & (y1==y5))) & \
        (not ((x1==x6) & (y1==y6))) & \
        (not ((x1==x7) & (y1==y7))) & \
        (not ((x1==x8) & (y1==y8))) & \
        (not ((x1==x9) & (y1==y9))) & \
        (not ((x1==x10) & (y1==y10))) & \
        (not ((x1==x11) & (y1==y11))) & \
        (not ((x1==x12) & (y1==y12))) & \
        (not ((x1==x13) & (y1==y13))) & \
        (not ((x1==x14) & (y1==y14))) & \
        (not ((x1==x15) & (y1==y15))) & \
        (not ((x2==x3) & (y2==y3))) & \
        (not ((x2==x4) & (y2==y4))) & \
        (not ((x2==x5) & (y2==y5))) & \
        (not ((x2==x6) & (y2==y6))) & \
        (not ((x2==x7) & (y2==y7))) & \
        (not ((x2==x8) & (y2==y8))) & \
        (not ((x2==x9) & (y2==y9))) & \
        (not ((x2==x10) & (y2==y10))) & \
        (not ((x2==x11) & (y2==y11))) & \
        (not ((x2==x12) & (y2==y12))) & \
        (not ((x2==x13) & (y2==y13))) & \
        (not ((x2==x14) & (y2==y14))) & \
        (not ((x2==x15) & (y2==y15))) & \
        (not ((x3==x4) & (y3==y4))) & \
        (not ((x3==x5) & (y3==y5))) & \
        (not ((x3==x6) & (y3==y6))) & \
        (not ((x3==x7) & (y3==y7))) & \
        (not ((x3==x8) & (y3==y8))) & \
        (not ((x3==x9) & (y3==y9))) & \
        (not ((x3==x10) & (y3==y10))) & \
        (not ((x3==x11) & (y3==y11))) & \
        (not ((x3==x12) & (y3==y12))) & \
        (not ((x3==x13) & (y3==y13))) & \
        (not ((x3==x14) & (y3==y14))) & \
        (not ((x3==x15) & (y3==y15))) & \
        (not ((x4==x5) & (y4==y5))) & \
        (not ((x4==x6) & (y4==y6))) & \
        (not ((x4==x7) & (y4==y7))) & \
        (not ((x4==x8) & (y4==y8))) & \
        (not ((x4==x9) & (y4==y9))) & \
        (not ((x4==x10) & (y4==y10))) & \
        (not ((x4==x11) & (y4==y11))) & \
        (not ((x4==x12) & (y4==y12))) & \
        (not ((x4==x13) & (y4==y13))) & \
        (not ((x4==x14) & (y4==y14))) & \
        (not ((x4==x15) & (y4==y15))) & \
        (not ((x5==x6) & (y5==y6))) & \
        (not ((x5==x7) & (y5==y7))) & \
        (not ((x5==x8) & (y5==y8))) & \
        (not ((x5==x9) & (y5==y9))) & \
        (not ((x5==x10) & (y5==y10))) & \
        (not ((x5==x11) & (y5==y11))) & \
        (not ((x5==x12) & (y5==y12))) & \
        (not ((x5==x13) & (y5==y13))) & \
        (not ((x5==x14) & (y5==y14))) & \
        (not ((x5==x15) & (y5==y15))) & \
        (not ((x6==x7) & (y6==y7))) & \
        (not ((x6==x8) & (y6==y8))) & \
        (not ((x6==x9) & (y6==y9))) & \
        (not ((x6==x10) & (y6==y10))) & \
        (not ((x6==x11) & (y6==y11))) & \
        (not ((x6==x12) & (y6==y12))) & \
        (not ((x6==x13) & (y6==y13))) & \
        (not ((x6==x14) & (y6==y14))) & \
        (not ((x6==x15) & (y6==y15))) & \
        (not ((x7==x8) & (y7==y8))) & \
        (not ((x7==x9) & (y7==y9))) & \
        (not ((x7==x10) & (y7==y10))) & \
        (not ((x7==x11) & (y7==y11))) & \
        (not ((x7==x12) & (y7==y12))) & \
        (not ((x7==x13) & (y7==y13))) & \
        (not ((x7==x14) & (y7==y14))) & \
        (not ((x7==x15) & (y7==y15))) & \
        (not ((x8==x9) & (y8==y9))) & \
        (not ((x8==x10) & (y8==y10))) & \
        (not ((x8==x11) & (y8==y11))) & \
        (not ((x8==x12) & (y8==y12))) & \
        (not ((x8==x13) & (y8==y13))) & \
        (not ((x8==x14) & (y8==y14))) & \
        (not ((x8==x15) & (y8==y15))) & \
        (not ((x9==x10) & (y9==y10))) & \
        (not ((x9==x11) & (y9==y11))) & \
        (not ((x9==x12) & (y9==y12))) & \
        (not ((x9==x13) & (y9==y13))) & \
        (not ((x9==x14) & (y9==y14))) & \
        (not ((x9==x15) & (y9==y15))) & \
        (not ((x10==x11) & (y10==y11))) & \
        (not ((x10==x12) & (y10==y12))) & \
        (not ((x10==x13) & (y10==y13))) & \
        (not ((x10==x14) & (y10==y14))) & \
        (not ((x10==x15) & (y10==y15))) & \
        (not ((x11==x12) & (y11==y12))) & \
        (not ((x11==x13) & (y11==y13))) & \
        (not ((x11==x14) & (y11==y14))) & \
        (not ((x11==x15) & (y11==y15))) & \
        (not ((x12==x13) & (y12==y13))) & \
        (not ((x12==x14) & (y12==y14))) & \
        (not ((x12==x15) & (y12==y15))) & \
        (not ((x13==x14) & (y13==y14))) & \
        (not ((x13==x15) & (y13==y15))) & \
        (not ((x14==x15) & (y14==y15))) \
        ):
        x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
        y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
        #print(x,y)
        try:
            slowa.append(slowo(x,y,matrix,16))
            TX.append(x)
            TY.append(y)
        except Exception:
            pass
                
        

#print(slowa)
#for ll in matrix:
#    print(ll)

with open('TX.csv','w') as result_file:
    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(TX)

with open('TY.csv','w') as result_file:
    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(TY)
    
with open('slowa.csv','w') as result_file:
    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(slowa)
                                                                        
#%%
print(f'TX= {len(TX)}')
print(f'TY= {len(TY)}')
print(f'slowa= {len(slowa)}')