# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:50:01 2020

@author: user
"""


import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import TensorBoard
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from textblob import TextBlob
import re
import time
import numpy as np
import matplotlib.pyplot as plt
import datetime


def get_time_period(year,month,day):
    current_date = datetime.datetime.today()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    days=0
    if(month > current_month):
        days += (current_year-1-year)*365
        if(day>current_day):
            days += ((12-month)+current_month-1)*30
            days += (31-day+current_day)
        else:
            days += (12-month+current_month)*30
            days +=(current_day-day)
    else:
        days += (current_year-year)*365
        if(day>current_day):
            days += (current_month-1-month)*30
            days += (31-day+current_day)
        else:
            days += (current_month-month)*30
            days +=(current_day-day)
    return days

def clean_tweet(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def analyze_sentiment(text):
    analysis = TextBlob(clean_tweet(text))
        
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

training_data = (pd.read_csv('training_data_2_csv.csv')) #load train csv file
training_data.head()

for i in range(0,len(training_data.description)):
    if(type(training_data.description[i])==float):
        training_data.description[i] = -1
    else:    
        training_data.description[i] = analyze_sentiment(training_data.description[i])

#for i in range(0,len(training_data.screen_name)):
#    if(type(training_data.screen_name[i])==float):
#        training_data.screen_name[i] = -1
#    else:    
#        training_data.screen_name[i] = analyze_sentiment(training_data.screen_name[i])

#for i in range(0,len(training_data.name)):
#    if(type(training_data.name[i])==float):
#        training_data.name[i] = -1
#    else:    
#        training_data.name[i] = analyze_sentiment(training_data.name[i])


#print(training_data['created_at'][0])
#print(len(training_data['created_at'][0]))
#print(training_data['created_at'][1])
#print(len(training_data['created_at'][1]))

#print(training_data['created_at'][2])
#print(len(training_data['created_at'][2]))
#print(training_data.created_at[1][6:8])
  
#print(training_data['created_at'][3])
#print(len(training_data['created_at'][3])) 

for i in range(0,len(training_data.created_at)):
    if(len(training_data.created_at[i])== 32):
        training_data.year[i] = int(training_data.created_at[i][27:31])
        training_data.day[i] = int(training_data.created_at[i][9:11])
        if(training_data.created_at[i][5:8]=="Jan"):
            training_data.month[i] = 1
        elif(training_data.created_at[i][5:8]=="Feb"):
            training_data.month[i] = 2
        elif(training_data.created_at[i][5:8]=="Mar"):
            training_data.month[i] = 3
        elif(training_data.created_at[i][5:8]=="Apr"):
            training_data.month[i] = 4
        elif(training_data.created_at[i][5:8]=="May"):
            training_data.month[i] = 5
        elif(training_data.created_at[i][5:8]=="Jun"):
            training_data.month[i] = 6
        elif(training_data.created_at[i][5:8]=="Jul"):
            training_data.month[i] = 7
        elif(training_data.created_at[i][5:8]=="Aug"):
            training_data.month[i] = 8
        elif(training_data.created_at[i][5:8]=="Sep"):
            training_data.month[i] = 9
        elif(training_data.created_at[i][5:8]=="Oct"):
            training_data.month[i] = 10
        elif(training_data.created_at[i][5:8]=="Nov"):
            training_data.month[i] = 11
        elif(training_data.created_at[i][5:8]=="Dec"):
            training_data.month[i] = 12
        else:
            training_data.month[i] = 0
    elif(len(training_data.created_at[i])== 30 or len(training_data.created_at[i])== 31):
        training_data.year[i] = int(training_data.created_at[i][26:30])
        training_data.day[i] = int(training_data.created_at[i][8:10])
        if(training_data.created_at[i][4:7]=="Jan"):
            training_data.month[i] = 1
        elif(training_data.created_at[i][4:7]=="Feb"):
            training_data.month[i] = 2
        elif(training_data.created_at[i][4:7]=="Mar"):
            training_data.month[i] = 3
        elif(training_data.created_at[i][4:7]=="Apr"):
            training_data.month[i] = 4
        elif(training_data.created_at[i][4:7]=="May"):
            training_data.month[i] = 5
        elif(training_data.created_at[i][4:7]=="Jun"):
            training_data.month[i] = 6
        elif(training_data.created_at[i][4:7]=="Jul"):
            training_data.month[i] = 7
        elif(training_data.created_at[i][4:7]=="Aug"):
            training_data.month[i] = 8
        elif(training_data.created_at[i][4:7]=="Sep"):
            training_data.month[i] = 9
        elif(training_data.created_at[i][4:7]=="Oct"):
            training_data.month[i] = 10
        elif(training_data.created_at[i][4:7]=="Nov"):
            training_data.month[i] = 11
        elif(training_data.created_at[i][4:7]=="Dec"):
            training_data.month[i] = 12
        else:
            training_data.month[i] = 0
    elif(len(training_data.created_at[i])==13 or (len(training_data.created_at[i])==14 and training_data.created_at[i][2:3]=='-')):
        training_data.year[i] = int('20'+training_data.created_at[i][6:8])
        training_data.day[i] = int(training_data.created_at[i][0:2])
        training_data.month[i] = int(training_data.created_at[i][3:5])
    elif((len(training_data.created_at[i])==15 and training_data.created_at[i][1:2]=='/') or len(training_data.created_at[i])==14):
        training_data.year[i] = int(training_data.created_at[i][5:9])
        training_data.day[i] = int(training_data.created_at[i][2:4])
        training_data.month[i] = int(training_data.created_at[i][0:1])
    elif((len(training_data.created_at[i])==15 and training_data.created_at[i][2:3]=='/') or len(training_data.created_at[i])==16):
        training_data.year[i] = int(training_data.created_at[i][6:10])
        training_data.day[i] = int(training_data.created_at[i][3:5])
        training_data.month[i] = int(training_data.created_at[i][0:2])
    else:
        print(training_data.created_at[i])
    
    training_data.duration[i]=get_time_period(training_data.year[i], training_data.month[i], training_data.day[i])
    
       
#print(training_data.year)
#print(training_data.month)
#print(training_data.day)

#print(training_data.screen_name)

training_data = training_data.sample(frac=1).reset_index(drop =True)

labels = training_data.iloc[:,-1].values
features =training_data.iloc[:,1:-1].values

#print(features[0,:])
features = np.delete(features, [4],1)

#print(features[0,:])

encode= LabelEncoder()
features[:,5] = encode.fit_transform(features[:,5])
features[:,7] = encode.fit_transform(features[:,7])
features[:,8] = encode.fit_transform(features[:,8])
features[:,9] = encode.fit_transform(features[:,9])
#features[:,11] = encode.fit_transform(features[:,11])






#print(features[0,:])

X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.2, random_state=0)

#print(training_data.duration)
logReg =LogisticRegression()

logReg.fit(X_train, Y_train)
prediction= logReg.predict(X_test)
print(accuracy_score(Y_test, prediction))
#prediction = prediction.tolist()
#Y_test = Y_test.tolist()
#ids = []
#for i in range(0,len(prediction)):
#    ids.append(i)

#plt.plot(ids,Y_test, label = 'test')
#plt.plot(ids,prediction, label = 'pred')
#plt.legend()
#plt.show()
#plt.figure(figsize=(20,4))
#plt.scatter(ids, Y_test)
#plt.scatter(ids, logReg.predict_proba(X_test)[:,1])
#plt.show()

#print(logReg.predict_proba(X_test))
#print(training_data['description'].value_counts())
#print(training_data.verified[0], training_data.default_profile[0], training_data.default_profile_image[0])
#l = [1, 1291, 0, 10, 0, 0, 78554, 1, 0, 0, 2017.0, 1.0, 2.0]
#l = np.array(l)
#print(features[0])
#print(logReg.predict([l]))
