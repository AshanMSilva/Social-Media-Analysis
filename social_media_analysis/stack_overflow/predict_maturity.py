#!/usr/bin/env python
# coding: utf-8

# In[1]:
import requests, traceback, json
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from stackpy import API, Site
import pickle
from datetime import datetime

class PredictMaturity:
    user_id = 0
    all_questions = []


    def __init__(self, user_id):
        self.user_id = user_id   
        
    def get_user_maturity(self):
        try:
            self.all_questions = self.get_all_questions(self.user_id)
            predict_data = self.convert_data_to_predictable(self.all_questions)
            predicted_data = self.get_predict_data(predict_data)
            self.all_questions['percentage'] = predicted_data['percentage']
            median_number = predicted_data['percentage'].median()
            median_number = round(median_number,1)
        except KeyError:
            median_number=0
            self.all_questions=[]
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

        #print(all_questions['closed_reason'])
        if not all_questions:
            return all_questions
        all_data = json_normalize(all_questions)
        all_data["creation_date"] = pd.to_datetime(all_data['creation_date'], unit='s').dt.strftime('%Y-%m-%d')
        # print(all_data["creation_date"])    
        # all_data = all_data.sort_values(by='creation_date',ascending=True)
        # print(all_data["creation_date"])
        return all_data
    
    def convert_data_to_predictable(self,df_nor):
        #Create a pandas data frame from normalized json data and sort its values according to 'score', 'answer_count',and 'view_count'
        newdf=pd.DataFrame(df_nor)
        newdf.reset_index(drop=True)
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
        filename="social_media_analysis/stack_overflow/finalized_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        predict_data["percentage"] = loaded_model.predict(predict_data)

        return predict_data

    def get_percentage_list(self):
        if( type(self.all_questions)!=list and not self.all_questions.empty):
            data = self.all_questions[["creation_date","percentage"]]
            data_points = []
            data=data.sort_values(by="creation_date",ascending=True)
            data = data.reset_index(drop=True)
            for i in range(len(data)) : 
                date = data.loc[i, "creation_date"]
                number = round(data.loc[i, "percentage"],1)
                record = {
                            "x" : date,
                            "y" : number
                        }
                data_points.append(record)
            data_points=json.dumps(data_points) 
            return data_points
        else:
            data=[]
            data=json.dumps([])
            return data

    def get_user_technologies(self):
        if(type(self.all_questions)!=list and not self.all_questions.empty):
            required_data = self.all_questions["tags"]
            languages = ["JavaScript","HTML","CSS","SQL","Python","Java","C#","PHP","C++","TypeScript","C","Ruby","Go","Assembly","Swift","Kotlin","R","VBA","Objective-C","Scala","Rust","Dart","Elixir","Clojure","F#","Erlang"]
            web_frameworks = ["jQuery","Reactjs","Angular","ASP.NET","Express","Spring","Vuejs","Django","Flask","Laravel","Ruby","Ruby-on-Rails","Drupal","Meteor","Ember.js"]
            other_frameworks = ["Nodejs",".NET",".Net-Core","Pandas","Unity3D","React-Native","Tenserflow","Ansible","Cordova","Xamarin","Apache-Spark","Hadoop","Unreal-Engine","Flutter","PyTorch","Puppet","Chef","CryEngine","SciPy","Numpy","Keras","Scikit-Learn","Eli5"]
            databases = ["MySQL","PostgreSQL","SQL-Server","SQLite","MongoDB","Redis","MariaDB","Oracle","ElasticSearch","Firebase","Amazon-DynamoDB","Cassandra","Couchbase"]
            platforms = ["Linux","Windows","Docker","Android","AWS","MacOS","Slack","Raspberry-Pi","WordPress","IOS","Google-Cloud-Platform","Azure","Arduino","Heroku","Kubernetes","IBM-Cloud"]

            lower_case_data = []

            languages_low = [i.lower() for i in languages]
            web_frameworks_low = [i.lower() for i in web_frameworks]
            other_frameworks_low = [i.lower() for i in other_frameworks]
            databases_low = [i.lower() for i in databases]
            platforms_low = [i.lower() for i in platforms]
            
            lower_case_data.extend(languages_low)
            lower_case_data.extend(web_frameworks_low)
            lower_case_data.extend(other_frameworks_low)
            lower_case_data.extend(databases_low)
            lower_case_data.extend(platforms_low)
            lower_case_data.extend(["python-3.x","python-2.7"])
            
            user_tecs = []
            temp_tags = []
            for tags in required_data:
                #cd stackprint(tags)
                '''tags = tags.replace("[","")
                tags = tags.replace("]","")
                tags = tags.replace("'","")
                tags = tags.split(",")'''
                tempTag = []
                for i in tags:
                    temp = i.strip()
                    if temp in lower_case_data:
                        if temp == "python" or temp == "python-3.x" or temp == "python-2.7":
                            if "python" not in tempTag:
                                tempTag.append("python")
                            if "python" not in user_tecs:
                                user_tecs.append("python")
                        else:
                            if temp not in tempTag:
                                tempTag.append(temp)
                            if temp not in user_tecs:
                                user_tecs.append(temp)
                temp_tags.append(tempTag)
            
            data = {}
            data["languages"] = []
            data["web_frameworks"] = []
            data["other_frameworks"] = []
            data["databases"] = []
            data["platforms"] = []
            #print(data)
            for tech in user_tecs:
                count = 0
                for techs in temp_tags:
                    if tech in techs:
                        count+=1
                percentage = count*100/len(temp_tags)
                percentage = round(percentage,1)
                name = ""
                if tech in languages_low:
                    name = languages[languages_low.index(tech)]
                    record = {
                                "name" : name,
                                "percentage" : percentage
                        
                            }
                    data["languages"].append(record)  
                elif tech in web_frameworks_low:
                    name = web_frameworks[web_frameworks_low.index(tech)]
                    record = {
                                "name" : name,
                                "percentage" : percentage
                        
                            }
                    data["web_frameworks"].append(record) 
                    
                elif tech in other_frameworks_low:
                    name = other_frameworks[other_frameworks_low.index(tech)]
                    record = {
                                "name" : name,
                                "percentage" : percentage
                        
                            }
                    data["other_frameworks"].append(record) 
                    
                elif tech in databases_low:
                    name = databases[databases_low.index(tech)]
                    record = {
                                "name" : name,
                                "percentage" : percentage
                        
                            }
                    data["databases"].append(record) 
                    
                elif tech in platforms_low:
                    name = platforms[platforms_low.index(tech)]
                    record = {
                                "name" : name,
                                "percentage" : percentage
                        
                            }
                    data["platforms"].append(record) 
            if not data["languages"] :
                data["languages"] = 0
            if not data["web_frameworks"] :
                data["web_frameworks"] = 0
            if not data["other_frameworks"] :
                data["other_frameworks"] = 0
            if not data["databases"] :
                data["databases"] = 0
            if not data["platforms"] :
                data["platforms"] = 0
            
                
            data=json.dumps(data)
            return data
        else:
            data=[]
            data=json.dumps([])
            return data







#c = PredictMaturity(20654)   

#print (c.get_user_maturity())
# print(c.get_percentage_list())
# print(c.get_user_technologies()) 



'''cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files)) '''

# In[ ]:




