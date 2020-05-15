#!/usr/bin/env python
# coding: utf-8

# In[1]:
import requests, traceback, json
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stackpy import API, Site
import pickle
from datetime import datetime

class PredictMaturity:
    user_id = 0
    all_questions = []


    def __init__(self, user_id):
        self.user_id = user_id   
        
    def get_user_maturity(self):
        self.all_questions = self.get_all_questions(self.user_id)
        predict_data = self.convert_data_to_predictable(self.all_questions)
        predicted_data = self.get_predict_data(predict_data)
        self.all_questions['percentage'] = predicted_data['percentage']
        median_number = predicted_data['percentage'].median()
        median_number = round(median_number,1)
        return median_number

    def get_all_questions(self,user):
        all_questions = []
        stack = "stackoverflow.com"
        page = 1
        while 1:
            u = f"https://api.stackexchange.com/2.2/users/{user}/questions?site={stack}&page={page}&pagesize=100"
            j = requests.get(u).json()
            if j:
                all_questions += j["items"]

                if not j['has_more']:
                    break
                elif not j['quota_remaining']:
                    break
            else:
                break

            page+=1
        if not all_questions:
            return all_questions
        all_data = json_normalize(all_questions)
        all_data["creation_date"] = pd.to_datetime(all_data['creation_date'], unit='s').dt.strftime('%Y-%m-%d')
            
        return all_data
    
    def convert_data_to_predictable(self,df_nor):
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

    def get_predict_data(self,predict_data):
        filename="finalized_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        predict_data["percentage"] = loaded_model.predict(predict_data)

        return predict_data

    def get_percentage_list(self):
        return self.all_questions[["creation_date","percentage"]]



















    



c = PredictMaturity(2593236)   

print (c.get_user_maturity())
c.get_percentage_list()


'''cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))'''

# In[ ]:




