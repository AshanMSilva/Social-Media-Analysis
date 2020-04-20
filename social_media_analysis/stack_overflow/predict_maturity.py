#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize
import json

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


def convert_data_to_predict(df_nor):
    #Create a pandas data frame from normalized json data and sort its values according to 'score', 'answer_count',and 'view_count'
    newdf=pd.DataFrame(df_nor)
    
    #remove null values and values in 'last_edit_date' column and replays it with 0 and 1
    change_last_edit=(newdf['last_edit_date'].notnull()).astype('int')
    newdf['last_edit_date']=change_last_edit
    
    #turn 'is_answered' values in to binary 
    newdf['is_answered']=newdf['is_answered'].astype(int)
    
    #Create new column 'is_closed' and check the whether the question is closed or not.
    newdf.loc[newdf['closed_reason'].isnull(), 'is_closed'] = 1
    newdf.loc[newdf['closed_reason'].notnull(), 'is_closed'] = 0
    
    #Convert 'tag_count', 'score', 'answer_count', 'view_count' columns to values to digital values 
    newdf['tag_count'] = newdf['tags'].str.len()
    newdf['score']=newdf['score'].clip(lower=0)
    newdf.loc[newdf['score'] >= 100, 'score'] = 100
    newdf.loc[newdf['answer_count'] > 5, 'answer_count'] = 5
    newdf.loc[newdf['view_count'] > 100, 'view_count'] = 100
    
    predict_data=newdf[['tag_count','is_answered','is_closed','view_count','answer_count','last_edit_date','score']]
    return predict_data
    
    
    


# In[ ]:




