from flask import render_template, url_for, flash, redirect, request, Blueprint,Flask, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
# from social_media_analysis.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
# from social_media_analysis.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import pickle
from datetime import datetime
from social_media_analysis.facebook.forms import AdForm
from bs4 import BeautifulSoup

#sentiment
import time 
import pandas as pd 
import matplotlib.pyplot as plt 
import nltk 
import io 
import operator
import unicodedata 
import numpy as np 
import re 
import string 
from numpy import linalg 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.corpus import webtext 
from nltk.stem.porter import PorterStemmer 
from nltk.stem.wordnet import WordNetLemmatizer 
from social_media_analysis.codes.FacebookCodes.post_like_prediction import LikePrediction 
from social_media_analysis.codes.FacebookCodes.ad_clicks_prediction import AdPrediction,AdImpressionPrediction,BestSolutions

import operator 
facebook = Blueprint('facebook', __name__)

@facebook.route('/sentimentAnalyser')
def sentimentAnalyser():
    return render_template('facebook_comments.html')
@facebook.route('/sentiment', methods=['POST'])
def sentiment():
        f=request.files['upload']

        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')
        comments=[]
        main_content = soup.find('ul', {'class': '_7a9a'})
        try:
            list_of_comments = main_content.findAll('li')
        except:
            main_content= soup.find('ul', {'class': '_7791'})
            list_of_comments = main_content.findAll('li')
        for container_large in list_of_comments:
            try:
                img_link= container_large.img.get('src')
                comment_container=container_large.find('div', {'class': '_72vr'})
                
                profile_link=comment_container.a.get('href')
                container_small = container_large.find('span', {'class': '_3l3x'})

                profile_name_container=comment_container.find('a', {'class': '_6qw4'})
                profile_name=profile_name_container.text
                lnk="C:/Users/Dane/Desktop"+img_link[1:]
                comments.append([container_small.text,profile_name,profile_link,lnk])
            except:
                x='s'
        check=[]
        pos=0
        neu=0
        neg=0
        pos_list=[]
        neu_list=[]
        neg_list=[]
        # scores_list=[]
        for i in range(len(comments)):
            try:
                comment=comments[i]
                text=comment[0]
                word=text
                sent_tokenizer = PunktSentenceTokenizer(text) 
                sents = sent_tokenizer.tokenize(text) 
                porter_stemmer = PorterStemmer()
                
                nltk_tokens = nltk.word_tokenize(text) 
                wordnet_lemmatizer = WordNetLemmatizer() 
                nltk_tokens = nltk.word_tokenize(text) 

                text = nltk.word_tokenize(text)
                sid = SentimentIntensityAnalyzer() 
                tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

                scores = sid.polarity_scores(word)
                c= scores['compound']
                del scores['compound']
                res=max(scores.items(), key=operator.itemgetter(1))[0]
                # comments[i].append(c)
                # comments[i].append(scores)
                if(res=='neu'):
                    neu_list.append(comments[i])
                elif(res=='pos'):
                    pos_list.append(comments[i])
                elif(res=='neg'):
                    neg_list.append(comments[i])
                neu+=scores['neu']
                pos+=scores['pos']
                neg+=scores['neg']

            except:
                print()
                #doing nothing
        pos_p=pos*100/(neg+pos+neu)
        neu_p=neu*100/(neg+pos+neu)
        neg_p=neg*100/(neg+pos+neu)
        post_result={"Negative":neg_p,"Positive":pos_p,"Neutral":neu_p}
        post_result["final"]=max(post_result.items(), key=operator.itemgetter(1))[0]
        all_comments=[pos_list,neu_list,neg_list]   
        return render_template('facebook_sentiment.html',check=check, all_comments=all_comments, post_result=post_result)

@facebook.route('/fbLikePredict',methods=['POST'])
def fbLikePredict():
    birthday=request.form["birthday"]
    gender=request.form["gender"]
    friendcount =request.form["friendcount"]
    birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    year = birthday.year
    month = birthday.month
    day = birthday.day
    if(gender=='Male'):
        gender=1
    if(gender=='Female'):
        gender=0
    year=int(year)
    day=int(day)
    month= int(month)
    gender=int(gender)
    friendcount=int(friendcount)
    final={'dob_day':[day] ,'dob_year':[year] ,'dob_month':[month] ,'gender':[gender] ,'friend_count':[friendcount] }
    final_features=pd.DataFrame.from_dict(final)
    prediction=LikePrediction()
    outputt=prediction.predict(final_features)
    # prediction = fbLikeModel.predict(final_features)
    output=int(outputt[0])
    return render_template('facebook_like_predict.html', prediction_text='Likes should be {}'.format(output))

@facebook.route('/fblikes')
def fblikes():
    return render_template('facebook_like_predict.html')


@facebook.route('/facebookAd')
def facebookAd():
    form=AdForm()
    return render_template('facebook_ad_clicks.html',form=form)


@facebook.route('/fbAdClicksPredict',methods=['POST'])
def fbAdClicksPredict():
    prediction=AdPrediction()
    day=request.form["weekday"]
    gender=request.form["gender"]
    txt =request.form["adText"]
    startAge = int(request.form["minAge"])
    endAge =int(request.form["maxAge"])
    # adImpressions =int(request.form["adImpressions"])
    adSpends =int(request.form["adSpends"])
    all=0
    male=0
    female=0
    if(gender=='M'):
        male=1
    if(gender=='F'):
        female=1
    if(gender=='A'):
        all=1
    mon=0
    tue=0
    wed=0
    thu=0
    fri=0
    sat=0
    sun=0
    if(day=='mon'):
        mon=1
    elif(day=='tue'):
        tue=1
    elif(day=='wed'):
        wed=1
    elif(day=='thu'):
        thu=1
    elif(day=='fri'):
        fri=1
    elif(day=='sat'):
        sat=1
    elif(day=='sun'):
        sun=1
    
    impre_final={'mon':[mon] ,'tue':[tue] ,'wed':[wed] ,'thu':[thu] ,'fri':[fri] ,'sat':[sat] ,'sun':[sun] ,'male':[male] ,'female':[female] ,'all':[all] ,'TextWordCount':[len(txt)] ,'startAge':[startAge] ,'endAge':[endAge],'AdSpends':[adSpends] }
    impre_final_features=pd.DataFrame.from_dict(impre_final)
    prediction_impre=AdImpressionPrediction()
    impre_outputt=prediction_impre.predict(impre_final_features)
    impre_output=int((impre_outputt[0]**2)**0.5)

    final={'mon':[mon] ,'tue':[tue] ,'wed':[wed] ,'thu':[thu] ,'fri':[fri] ,'sat':[sat] ,'sun':[sun] ,'male':[male] ,'female':[female] ,'all':[all] ,'TextWordCount':[len(txt.split())] ,'startAge':[startAge] ,'endAge':[endAge],'AdImpressions':[impre_output],'AdSpends':[adSpends] }
    final_features=pd.DataFrame.from_dict(final)
    prediction=AdPrediction()
    outputt=prediction.predict(final_features)
    output=int((outputt[0]**2)**0.5)
    impre_prediction=AdImpressionPrediction()
    bestSolutions=BestSolutions()
    best_results=[bestSolutions.getBestGender(final,prediction),bestSolutions.getBestSpend(impre_final,prediction,impre_prediction),bestSolutions.getBestWeekDay(final,prediction)    ]

    return render_template('facebook_ad_display.html', results={'impressions':impre_output,'clicks':output},best_results=best_results )