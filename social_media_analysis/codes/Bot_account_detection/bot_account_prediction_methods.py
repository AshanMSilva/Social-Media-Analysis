# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:30:46 2020

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
import pickle


class Prediction():
    def sentiment_description(self, description):
        if(type(description)==float or description == ''):
            description = -1
        else:    
            description = self.analyze_sentiment(description)
        return description
    
    def clean_tweet(self, text):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

    def analyze_sentiment(self, text):
        analysis = TextBlob(self.clean_tweet(text))
            
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
    
    def get_date(self, created_at):
        if(len(created_at)== 32):
            year = int(created_at[27:31])
            day = int(created_at[9:11])
            if(created_at[5:8]=="Jan"):
                month = 1
            elif(created_at[5:8]=="Feb"):
                month = 2
            elif(created_at[5:8]=="Mar"):
                month = 3
            elif(created_at[5:8]=="Apr"):
                month = 4
            elif(created_at[5:8]=="May"):
                month = 5
            elif(created_at[5:8]=="Jun"):
                month = 6
            elif(created_at[5:8]=="Jul"):
                month = 7
            elif(created_at[5:8]=="Aug"):
                month = 8
            elif(created_at[5:8]=="Sep"):
                month = 9
            elif(created_at[5:8]=="Oct"):
                month = 10
            elif(created_at[5:8]=="Nov"):
                month = 11
            elif(created_at[5:8]=="Dec"):
                month = 12
            else:
                month = 0
        elif(len(created_at)== 30 or len(created_at)== 31):
            year = int(created_at[26:30])
            day = int(created_at[8:10])
            if(created_at[4:7]=="Jan"):
                month = 1
            elif(created_at[4:7]=="Feb"):
                month = 2
            elif(created_at[4:7]=="Mar"):
                month = 3
            elif(created_at[4:7]=="Apr"):
                month = 4
            elif(created_at[4:7]=="May"):
                month = 5
            elif(created_at[4:7]=="Jun"):
                month = 6
            elif(created_at[4:7]=="Jul"):
                month = 7
            elif(created_at[4:7]=="Aug"):
                month = 8
            elif(created_at[4:7]=="Sep"):
                month = 9
            elif(created_at[4:7]=="Oct"):
                month = 10
            elif(created_at[4:7]=="Nov"):
                month = 11
            elif(created_at[4:7]=="Dec"):
                month = 12
            else:
                month = 0
        elif(len(created_at)==13 or (len(created_at)==14 and created_at[2:3]=='-')):
            year = int('20'+created_at[6:8])
            day = int(created_at[0:2])
            month = int(created_at[3:5])
        elif((len(created_at)==15 and created_at[1:2]=='/') or len(created_at)==14):
            year = int(created_at[5:9])
            day = int(created_at[2:4])
            month = int(created_at[0:1])
        elif((len(created_at)==15 and created_at[2:3]=='/') or len(created_at)==16):
            year = int(created_at[6:10])
            day = int(created_at[3:5])
            month = int(created_at[0:2])
        else:
            year = 0
            day = 0
            month = 0
        return year,month,day
    
    def encode_verified(self, verified):
        if(verified == 'FALSE' or verified == 'false' or verified == False):
            verified = 0
        elif(verified == 'TRUE' or verified == 'true' or verified == True):
            verified = 1
        else:
            verified = -1
        return verified
    
    def encode_default_profile(self, default_profile):
        if(default_profile == 'FALSE' or default_profile == 'false' or default_profile == False):
            default_profile = 0
        elif(default_profile == 'TRUE' or default_profile == 'true' or default_profile == False):
            default_profile = 1
        else:
            default_profile = -1
        return default_profile
    
    def encode_default_profile_image(self, default_profile_image):
        if(default_profile_image == 'FALSE' or default_profile_image == 'false' or default_profile_image == False):
            default_profile_image = 0
        elif(default_profile_image == 'TRUE' or default_profile_image == 'true' or default_profile_image == True):
            default_profile_image = 1
        else:
            default_profile_image = -1
        return default_profile_image
    
    def encode_has_extended_profile(self, has_extended_profile):
        if(has_extended_profile == 'FALSE' or has_extended_profile == 'false' or has_extended_profile == False):
            has_extended_profile = 0
        elif(has_extended_profile == 'TRUE' or has_extended_profile == 'true' or has_extended_profile == True):
            has_extended_profile = 1
        else:
            has_extended_profile = -1
        return has_extended_profile

    def get_time_period(self, year,month,day):
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

    def predict(self, pred_list):
        filename = 'social_media_analysis/codes/Bot_account_detection/finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict_proba(pred_list)*100
        return result[0]
l =[0, 29, 5, 0, 5, 0, 36, -1, 0, 1, 2017, 2, 25, 1124]
