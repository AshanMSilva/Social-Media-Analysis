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


facebook = Blueprint('facebook', __name__)
# import os
# SECRET_KEY = os.urandom(32)
# facebook.config['SECRET_KEY'] = SECRET_KEY

# instaModel = pickle.load(open('instamodel.pkl', 'rb')) 
# fbLikeModel = pickle.load(open('url_for{{fbLikeModel.pkl}}', 'rb'))
# fbAdsModel =pickle.load(open('fbAdsModel.pkl', 'rb')) 


@facebook.route('/sentimentAnalyser')
def sentimentAnalyser():
    return render_template('facebook_sentiment.html')
@facebook.route('/sentiment', methods=['POST'])
def sentiment():
        text=request.form['txt']
        tt=text
        sent_tokenizer = PunktSentenceTokenizer(text) 
        sents = sent_tokenizer.tokenize(text) 
        porter_stemmer = PorterStemmer()
        
        nltk_tokens = nltk.word_tokenize(text) 
        wordnet_lemmatizer = WordNetLemmatizer() 
        nltk_tokens = nltk.word_tokenize(text) 

        text = nltk.word_tokenize(text)
        sid = SentimentIntensityAnalyzer() 
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

        for word in tt.split("\n"): 
                print(word)
                scores = sid.polarity_scores(word)
                c= scores['compound']
                del scores['compound']
                res=max(scores, key=scores.get)


                #res= max(scores.iteritems(), key=operator.itemgetter(1))[0]
        return render_template('facebook_sentiment.html', prediction_text='The comment is {}'.format(res), msg=c)

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
    impre_output=int(impre_outputt[0])

    final={'mon':[mon] ,'tue':[tue] ,'wed':[wed] ,'thu':[thu] ,'fri':[fri] ,'sat':[sat] ,'sun':[sun] ,'male':[male] ,'female':[female] ,'all':[all] ,'TextWordCount':[len(txt.split())] ,'startAge':[startAge] ,'endAge':[endAge],'AdImpressions':[impre_output],'AdSpends':[adSpends] }
    final_features=pd.DataFrame.from_dict(final)
    prediction=AdPrediction()
    outputt=prediction.predict(final_features)
    output=int(outputt[0])

    bestSolutions=BestSolutions()
    best_results=[bestSolutions.getBestGender(final,prediction),bestSolutions.getBestSpend(final,prediction),bestSolutions.getBestWeekDay(final,prediction)    ]
    # best_results=[bestSolutions.getBestGender(final,prediction)]


    # return render_template('facebook_ad_display.html', impre_prediction_text='clicks should be {}'.format(output) )
    return render_template('facebook_ad_display.html', results={'impressions':impre_output,'clicks':output},best_results=best_results )