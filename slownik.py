# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:52:54 2020

@author: Ja
"""

import pandas as pd
import słowotok as st

#%%

slownik=pd.read_csv('slowa.txt', sep="\n", header=None)
slownik.columns=['col1']
print(slownik.col1.map(len).max())

#%%

slownik=slownik.loc[slownik['col1'].str.len()>=15]
slownik=slownik.loc[slownik['col1'].str.len()<=16]

#%%
matrix=st.gen_table()

#%%
print(slownik)