# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:38:08 2021

@author: Ja
"""
M=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

i0=1
j0=1

def add_next(i0,j0,Sn_in):
    Sn_out=[]
    for s in Sn_in:
        for j in [-1,0,1]:
            for i in [-1,0,1]:
                if ((j0+j<0) or (i0+i<0) or (j==0 and i==0)):
                    continue
                Sn_tmp=s.copy()
                Sn_tmp.append(M[j0+j][i0+i])
                Sn_out.append(Sn_tmp)
    return Sn_out
            #print(M[j0+j][i0+i])

def czy_dubel(x,y,S_in):
    if [x,y] in S_in:
        return True
    else:
        return False

dim=[0,1,2,3]
S=[]            
for i1 in dim:
    for j1 in dim:
        for i2 in [-1,0,1]:
            for j2 in [-1,0,1]:
                is1=i1+i2
                js1=j1+j2
                if ((is1<0) or (is1>3) or (js1<0) or (js1>3) or (i2==0 and j2==0)):
                    continue
                #S.append([M[i1][j1],M[is1][js1]])
                for i3 in [-1,0,1]:
                    for j3 in [-1,0,1]:
                        is2=i1+i2+i3
                        js2=j1+j2+j3
                        if ((is2<0) or (is2>3) or (js2<0) or (js2>3) or (i3==0 and j3==0)):
                            continue
                        W=[[i1,j1],[is1,js1]]
                        if czy_dubel(is2,js2,W):
                            continue
                        S.append([M[i1][j1],M[is1][js1],M[is2][js2]])
                        
                        for i4 in [-1,0,1]:
                            for j4 in [-1,0,1]:
                                is3=i1+i2+i3+i4
                                js3=j1+j2+j3+j4
                                if ((is3<0) or (is3>3) or (js3<0) or (js3>3) or (i4==0 and j4==0)):
                                    continue
                                W.append([is2,js2])
                                if czy_dubel(is3,js3,W):
                                    continue
                                S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3]])
'''                                
                                for i5 in [-1,0,1]:
                                    for j5 in [-1,0,1]:
                                        is4=i1+i2+i3+i4+i5
                                        js4=j1+j2+j3+j4+j5
                                        if ((is4<0) or (is4>3) or (js4<0) or (js4>3) or (i5==0 and j5==0)):
                                            continue
                                        W.append([is3,js3])
                                        if czy_dubel(is4,js4,W):
                                            continue
                                        S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4]])
                                        
                                        for i6 in [-1,0,1]:
                                            for j6 in [-1,0,1]:
                                                is5=i1+i2+i3+i4+i5+i6
                                                js5=j1+j2+j3+j4+j5+j6
                                                if ((is5<0) or (is5>3) or (js5<0) or (js5>3) or (i6==0 and j6==0)):
                                                    continue
                                                W.append([is4,js4])
                                                if czy_dubel(is5,js5,W):
                                                    continue
                                                S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4],M[is5][js5]])

                                                for i7 in [-1,0,1]:
                                                    for j7 in [-1,0,1]:
                                                        is6=i1+i2+i3+i4+i5+i6+i7
                                                        js6=j1+j2+j3+j4+j5+j6+j7
                                                        if ((is6<0) or (is6>3) or (js6<0) or (js6>3) or (i7==0 and j7==0)):
                                                            continue
                                                        W.append([is5,js5])
                                                        if czy_dubel(is6,js6,W):
                                                            continue
                                                        S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4],M[is5][js5],M[is6][js6]])

                                                        for i8 in [-1,0,1]:
                                                            for j8 in [-1,0,1]:
                                                                is7=i1+i2+i3+i4+i5+i6+i7+i8
                                                                js7=j1+j2+j3+j4+j5+j6+j7+j8
                                                                if ((is7<0) or (is7>3) or (js7<0) or (js7>3) or (i8==0 and j8==0)):
                                                                    continue
                                                                W.append([is6,js6])
                                                                if czy_dubel(is7,js7,W):
                                                                    continue
                                                                S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4],M[is5][js5],M[is6][js6],M[is7][js7]])

                                                                for i9 in [-1,0,1]:
                                                                    for j9 in [-1,0,1]:
                                                                        is8=i1+i2+i3+i4+i5+i6+i7+i8+i9
                                                                        js8=j1+j2+j3+j4+j5+j6+j7+j8+j9
                                                                        if ((is8<0) or (is8>3) or (js8<0) or (js8>3) or (i9==0 and j9==0)):
                                                                            continue
                                                                        W.append([is7,js7])
                                                                        if czy_dubel(is8,js8,W):
                                                                            continue
                                                                        S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4],M[is5][js5],M[is6][js6],M[is7][js7],M[is8][js8]])

                                                                        for i10 in [-1,0,1]:
                                                                            for j10 in [-1,0,1]:
                                                                                is9=i1+i2+i3+i4+i5+i6+i7+i8+i9+i10
                                                                                js9=j1+j2+j3+j4+j5+j6+j7+j8+j9+j10
                                                                                if ((is9<0) or (is9>3) or (js9<0) or (js9>3) or (i10==0 and j10==0)):
                                                                                    continue
                                                                                W.append([is8,js8])
                                                                                if czy_dubel(is9,js9,W):
                                                                                    continue
                                                                                S.append([M[i1][j1],M[is1][js1],M[is2][js2],M[is3][js3],M[is4][js4],M[is5][js5],M[is6][js6],M[is7][js7],M[is8][js8],M[is9][js9]])

'''                                                                                
print(S)