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
import cssutils

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
        #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################
   
    return render_template('facebook_comments.html',registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
@facebook.route('/sentiment', methods=['POST'])
def sentiment():
        #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################
    pos_imojies= {'1f600': 0.2, '1f603': 0.2, '1f604': 0.2, '1f601': 0.2, '1f606': 0.2, '1f605': 0.2, '1f602': 0.2, '1f923': 0.2, '263a': 0.1, '1f60a': 0.1, '1f607': 0.1, '1f642': 0.2, '1f643': 0.1, '1f609': 0.1, '1f60d': 0.3, '1f970': 0.3, '1f618': 0.3, '1f617': 0.3, '1f619': 0.3, '1f61a': 0.3, '1f60b': 0.3, '1f61b': 0.3, '1f61d': 0.3, '1f61c': 0.3, '1f92a': 0.3, '1f60e': 0.1, '1f929': 0.3, '1f973': 0.3, '1f917': 0.2, '1f92d': 0.1, '1f636': 0.3, '1f62c': 0.3, '1f912': 0.2, '1f911': 0.2, '1f921': 0.1, '1f4a9': 0.3, '1f47b': 0.3, '1f480': 0.3, '2620': 0.3, '1f47e': 0.3, '1f639': 0.2, '1f63b': 0.2, '1f63c': 0.2, '1f63d': 0.2, '1f640': 0.2, '1f63f': 0.2, '1f63e': 0.2, '1f932': 0.2, '1f450': 0.2, '1f64c': 0.2, '1f44f': 0.2, '1f91d': 0.2, '1f44d': 0.2, '1f44e': 0.2, '1f44a': 0.2, '270a': 0.2, '1f91b': 0.2, '1f91c': 0.2, '1f91e': 0.2, '270c': 0.2, '1f91f': 0.2, '1f918': 0.2, '1f44c': 0.2, '1f448': 0.2, '1f449': 0.2, '1f446': 0.2, '1f447': 0.2, '261d': 0.2, '270b': 0.2, '1f91a': 0.2, '1f590': 0.2, '1f596': 0.2, '2764': 0.3, '1f9e1': 0.3, '1f49b': 0.3, '1f49a': 0.3, '1f499': 0.3, '1f49c': 0.3, '1f5a4': 0.3, '2763': 0.3, '1f495': 0.3, '1f49e': 0.3, '1f493': 0.3, '1f497': 0.3, '1f496': 0.3, '1f498': 0.3, '1f49d': 0.3, '1f49f': 0.3, '262e': 0.3, '271d': 0.3, '262a': 0.3, '1f549': 0.3, '2638': 0.3, '2721': 0.3, '1f52f': 0.3}
    
    neu_imojies={'1f60c': 0.3, '1f9d0': 0.2, '1f913': 0.2, '1f914': 0.2, '1f92b': 0.2, '1f925': 0.2, '1f610': 0.2, '1f611': 0.2, '1f626': 0.2, '1f479': 0.1, '1f47a': 0.1, '1f47d': 0.3, '1f916': 0.3, '1f638': 0.3}

    neg_imojies={'1f928': 0.3, '1f60f': 0.3, '1f612': 0.3, '1f61e': 0.3, '1f614': 0.3, '1f61f': 0.3, '1f615': 0.3, '1f641': 0.3, '2639': 0.3, '1f623': 0.3, '1f616': 0.3, '1f62b': 0.3, '1f629': 0.3, '1f97a': 0.3, '1f622': 0.3, '1f62d': 0.3, '1f624': 0.3, '1f620': 0.3, '1f621': 0.3, '1f92c': 0.3, '1f92f': 0.3, '1f633': 0.3, '1f975': 0.3, '1f976': 0.3, '1f631': 0.3, '1f628': 0.3, '1f630': 0.3, '1f625': 0.3, '1f613': 0.2, '1f644': 0.3, '1f62f': 0.3, '1f627': 0.3, '1f62e': 0.3, '1f632': 0.3, '1f634': 0.3, '1f924': 0.3, '1f62a': 0.3, '1f635': 0.3, '1f910': 0.3, '1f974': 0.3, '1f922': 0.3, '1f92e': 0.3, '1f927': 0.3, '1f637': 0.3, '1f915': 0.3, '1f920': 0.3, '1f608': 0.3, '1f47f': 0.3, '1f383': 0.1, '1f63a': 0.3, '1f494': 0.3}
    
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
            container_small = container_large.find('span', {'class': '_3l3x'}) #imoji spnas & text in here
            imoji_spans=container_small.findAll('span', {'class': '_5mfr'})
            imojies=[]
            for imoji_span in imoji_spans:
                span_style=imoji_span.find('span')['style']
                style=cssutils.parseStyle(span_style)
                imoji_url=style['background-image']
                imojies.append((imoji_url.split('/'))[-1].split('.')[0])
            profile_name_container=comment_container.find('a', {'class': '_6qw4'})
            profile_name=profile_name_container.text
            lnk="C:/Users/Dane/Desktop"+img_link[1:]
            comments.append([container_small.text,profile_name,profile_link,lnk,imojies])
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

            # add imoji values
            imojies=comments[i][4]
            if(len(imojies)>0):
                neg_temp=scores['neg']
                pos_temp=scores['pos']
                neu_temp=scores['neu']
                scores['neg']=0
                scores['pos']=0
                scores['neu']=0
                found=False
            for imoji in imojies:
                if(imoji in pos_imojies):
                    scores['pos']+=pos_imojies[imoji]
                    found=True
                elif(imoji in neu_imojies):
                    found=True
                    scores['neu']+=neu_imojies[imoji]
                elif(imoji in neg_imojies):
                    found=True
                    scores['neg']+=neg_imojies[imoji]                
            if(found==False):
                scores['neg']=neg_temp
                scores['pos']=pos_temp
                scores['neu']=neu_temp
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
    form=AdForm()
    return render_template('facebook_sentiment.html',form=form, all_comments=all_comments, post_result=post_result,registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)

@facebook.route('/fbLikePredict',methods=['POST'])
def fbLikePredict():
        #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################
   
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
    return render_template('facebook_like_predict.html', prediction_text='Likes should be {}'.format(output,registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow))

@facebook.route('/fblikes')
def fblikes():
            #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################
   
    return render_template('facebook_like_predict.html',registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)


@facebook.route('/facebookAd')
def facebookAd():
    #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################

    form=AdForm()
    return render_template('facebook_ad_clicks.html',form=form, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)


@facebook.route('/fbAdClicksPredict',methods=['POST'])
def fbAdClicksPredict():
        #common ligin and signin routes
    loginmodalshow='close'
    loginform = LoginForm()
    if(loginform.validate_on_submit()==False and loginform.login.data):
        loginmodalshow='loginformmodal'
    if loginform.validate_on_submit() and loginform.login.data:
        remember=loginform.remember.data
        email=loginform.email.data
        password=loginform.password.data
        return redirect(url_for('users.login', remember=remember, email=email, password=password))
    modalshow='close'
    registerform = RegistrationForm()
    if(registerform.validate_on_submit()==False and registerform.signup.data):
        modalshow='registerformmodal' 
    if registerform.validate_on_submit() and registerform.signup.data:
        username=registerform.username.data
        email=registerform.email.data
        password=registerform.password.data
        return redirect(url_for('users.register', username=username, email=email, password=password))
    ################################
   
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
    form=AdForm()
    return render_template('facebook_ad_display.html',form=form,registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow, results={'impressions':impre_output,'clicks':output},best_results=best_results )