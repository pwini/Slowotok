#! C:\Users\piotr_000\AppData\Local\Programs\Python\Python35-32 python
# -*- coding: utf-8 -*-

import random
#import itertools
import csv

def slowo(X,Y,tab,n):
    sl=''
    for i in range(n):
        sl=sl+tab[X[i]][Y[i]]
    return sl

def generic(TX, TY, matrix, k):

    print(f'{k} letters word')
    
    
    XK=[]
    YK=[]
    for xk,yk in zip(TX,TY):
        for i in range(3):
            for j in range(3):
                repeated_item=False
                xk_1=xk[k-2]+i-1
                yk_1=yk[k-2]+j-1
                if ((xk_1>=0) & (yk_1>=0) & (xk_1<=3) & (yk_1<=3)):
                    for l in range(k-1):
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
                        slowa.append(slowo(x_tmp, y_tmp, matrix,k))
    #TX=TX+XK
    #TY=TY+YK
    return XK, YK


def gen_table():
    # Collect letters from polish language
    chr_n=[211, 260, 262, 280, 321, 323, 346, 377, 379]
    for i in range (65,91):
        chr_n.append(i)
        
    # Generate artificial letter matrix
    matrix=[[chr(chr_n[random.randint(0, 34)]) for i in range(4)] for j in range(4)]
    return matrix
# Find all possible words in matrix

#for i in matrix:
#    print(i)

slowa=[]
TX=[]
TY=[]
''
#
#X0=set([0,1,2,3])
#Y0=set([0,1,2,3])

#xn=set([0,1,2])
#yn=set([0,1,2])

#
#for s in slowa:
#    print(s)

#
    
#print(len(slowa))


#%%
                          
matrix=gen_table()
matrix=[['1','2','3','4'],['5','6','7','8'],['9','A','B','C'],['D','E','F','G']]

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




TX_4, TY_4 = generic(TX,TY,matrix,4)


#%%
TX_5, TY_5 = generic(TX_4,TY_4,matrix,5)

#%%
TX_6, TY_6 = generic(TX_5,TY_5,matrix,6)

#%%
TX_7, TY_7 = generic(TX_6,TY_6,matrix,7)

#%%
TX_8, TY_8 = generic(TX_7,TY_7,matrix,8)

#%%
TX_9, TY_9 = generic(TX_8,TY_8,matrix,9)

#%%
TX_10, TY_10 = generic(TX_9,TY_9,matrix,10)

#%%
TX_11, TY_11 = generic(TX_10,TY_10,matrix,11)

#%%
TX_12, TY_12 = generic(TX_11,TY_11,matrix,12)

#%%
TX_13, TY_13 = generic(TX_12,TY_12,matrix,13)

#%%
TX_14, TY_14 = generic(TX_13,TY_13,matrix,14)

#%%
TX_15, TY_15 = generic(TX_14,TY_14,matrix,15)

#%%
TX_16, TY_16 = generic(TX_15,TY_15,matrix,16)

#%% Nieaktywne


#%% Statystyki

#print(f'TX= {len(TX)}')
#print(f'TY= {len(TY)}')
print(f'slowa= {len(slowa)}')
     
#%% Połaczenie wszystkich współrzędnych
#print('sumowanie TX i TY')
#TX=TX+TX_4+TX_5+TX_6+TX_7+TX_8+TX_9+TX_10+TX_11+TX_12+TX_13+TX_14+TX_15+TX_16
#TY=TY+TY_4+TY_5+TY_6+TY_7+TY_8+TY_9+TY_10+TY_11+TY_12+TY_13+TY_14+TY_15+TY_16

#%% Zapis TX
#print('zapisywanie TX')
#with open('TX.csv','w') as result_file:
#    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
#    wr.writerow(TX)

#%% Zapis TY
#print('zapisywanie TY')
#with open('TY.csv','w') as result_file:
#    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
#    wr.writerow(TY)

#%% Zapis slowa    
print('zapisywanie slowa')
with open('slowa.csv','w') as result_file:
    wr = csv.writer(result_file, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(slowa)

#%%    