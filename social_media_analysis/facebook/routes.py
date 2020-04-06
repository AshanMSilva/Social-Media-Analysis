from flask import render_template, url_for, flash, redirect, request, Blueprint,Flask, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from social_media_analysis.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
from social_media_analysis.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import pickle
from datetime import datetime


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

facebook = Blueprint('facebook', __name__)


@facebook.route('/sentimentAnalyser')
def sentimentAnalyser():
    return render_template('sentiment.html')
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
        return render_template('sentiment.html', prediction_text='The comment is {}'.format(res), msg=c)

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
    prediction = fbLikeModel.predict(final_features)
    output=int(prediction[0])
    
    # output = round(prediction[0], 2)

    return render_template('facebookLike.html', prediction_text='Likes should be {}'.format(output))

@facebook.route('/fblikes')
def fblikes():
    return render_template('facebookLike.html')
