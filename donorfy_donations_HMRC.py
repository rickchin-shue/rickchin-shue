# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:52:05 2022

@author: Lenovo
"""

import pandas as pd
import numpy as np
import os


filename = 'DonationsGiftAid.csv'
df = pd.read_csv(filename)

colren = {'First name or initial':'firstname', 'Last name':'lastname', 'House name or number':'address1','Donation date':'date'}
df.rename(columns=colren, inplace=True)
df.head()

df.drop(columns =[ 'Title','Aggregated donations', 'Sponsored event'], inplace=True)
df
x = df.sort_values('date')
x['date2'] = pd.to_datetime( df['date'] )
x.head()
x = x.sort_values('date2')
x.head()

x['fullname'] = x.lastname + '.' + x.firstname




y = x.groupby('fullname').agg({'date2':['count','min','max']})
y.sort_values(('date2','count'), ascending=False, inplace=True)
y.head(10)
