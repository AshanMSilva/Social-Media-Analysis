# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:58:31 2020

@author: user
"""

import pandas as pd
 
data = (pd.read_csv('codes/ViralVideoAnalysis/analysedData.csv'))

language = (data.iloc[:,6].values)

print(data)
print(language)