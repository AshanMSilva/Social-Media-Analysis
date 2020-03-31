from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from social_media_analysis.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
from social_media_analysis.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import numpy as np
import pickle
from social_media_analysis.codes.Tweet_Likes_Prediction.tweet_likes_prediction import TweetLikesPrediction

twitter = Blueprint('twitter', __name__)


@twitter.route("/twitter/<string:name>")
@login_required
def user_details(name):
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
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    user = twitter_client.get_user(name)
    tweets = twitter_client.get_tweets_of_a_user(name, 100)
    replies = 0
    mentions =0
    hashtags =0
    retweets=0
    links =0
    medias=0
    zero=0
    one =0
    two=0
    three=0
    four=0
    five=0
    six=0
    seven=0
    eight=0
    nine=0
    ten=0
    eleven=0
    twelve=0
    thirteen=0
    fourteen=0
    fifteen=0
    sixteen=0
    seventeen=0
    eighteen=0
    nineteen=0
    twenty=0
    twentyone=0
    twentytwo=0
    twentythree=0
    ids=[]
    favourites=[]
    for tweet in tweets:
        if(len(tweet.entities['hashtags'])>0):
            hashtags+=1
        if(len(tweet.entities['user_mentions'])>0):
            mentions+=1
        if(len(tweet.entities['urls'])>0):
            links+=1
        if('media' in tweet.entities):
            if(len(tweet.entities['media'])>0):
                medias+=1
        if(hasattr(tweet, 'retweeted_status')):
            retweets+=1
        if(tweet.in_reply_to_status_id !=None):
            replies+=1
        if(tweet.created_at.hour == 0):
            zero+=1
        if(tweet.created_at.hour == 1):
            one+=1
        if(tweet.created_at.hour == 2):
            two+=1
        if(tweet.created_at.hour == 3):
            three+=1
        if(tweet.created_at.hour == 4):
            four+=1
        if(tweet.created_at.hour == 5):
            five+=1
        if(tweet.created_at.hour == 6):
            six+=1
        if(tweet.created_at.hour == 7):
            seven+=1
        if(tweet.created_at.hour == 8):
            eight+=1
        if(tweet.created_at.hour == 9):
            nine+=1
        if(tweet.created_at.hour == 10):
            ten+=1
        if(tweet.created_at.hour == 11):
            eleven+=1
        if(tweet.created_at.hour == 12):
            twelve+=1
        if(tweet.created_at.hour == 13):
            thirteen+=1
        if(tweet.created_at.hour == 14):
            fourteen+=1
        if(tweet.created_at.hour == 15):
            fifteen+=1
        if(tweet.created_at.hour == 16):
            sixteen+=1
        if(tweet.created_at.hour == 17):
            seventeen+=1
        if(tweet.created_at.hour == 18):
            eighteen+=1
        if(tweet.created_at.hour == 19):
            nineteen+=1
        if(tweet.created_at.hour == 20):
            twenty+=1
        if(tweet.created_at.hour == 21):
            twentyone+=1
        if(tweet.created_at.hour == 22):
            twentytwo+=1
        if(tweet.created_at.hour == 23):
            twentythree+=1
        ids.append(tweet.id)
        favourites.append(tweet.favorite_count)
    tweetsdata ={
        "hashtags": hashtags,
        "mentions": mentions,
        "links": links,
        "medias":medias,
        "retweets":retweets,
        "replies":replies
    }
    graphdata ={
        "0":zero,
        "1":one,
        "2":two,
        "3":three,
        "4":four,
        "5":five,
        "6":six,
        "7":seven,
        "8":eight,
        "9":nine,
        "10":ten,
        "11":eleven,
        "12":twelve,
        "13":thirteen,
        "14":fourteen,
        "15":fifteen,
        "16":sixteen,
        "17":seventeen,
        "18":eighteen,
        "19":nineteen,
        "20":twenty,
        "21":twentyone,
        "22":twentytwo,
        "23":twentythree   
    }
    verified='NOTVERIFIED'
    badge='badge-danger'
    if(user.verified):
        verified='VERIFIED'
        badge='badge-success'
    
    return render_template('user_details.html', user=user, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow, tweetsdata=tweetsdata, verified=verified, badge=badge, graphdata=graphdata, ids=ids, favourites=favourites)



@twitter.route("/twitter/hashtag/<string:hashtag>")
@login_required
def hashtag_tweets(hashtag):
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
    hasht = '#'+hashtag
    twitter_client = TwitterClient()
    tweets = twitter_client.get_similar_tweets(hasht, 'recent', 1)
    return render_template('hashtag.html', tweets=tweets, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)

@twitter.route("/twitter/botaccount/<string:name>")
@login_required
def bot_account_detection(name):
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
    twitter_client = TwitterClient()
    user = twitter_client.get_user(name)
    prediction = Prediction()
    created_at = user.created_at
    year = created_at.year
    month = created_at.month
    day = created_at.day
    duration = prediction.get_time_period(year,month,day)
    id = user.id
    description = prediction.sentiment_description(user.description)
    followers_count = user.followers_count
    friends_count = user.friends_count
    listed_count = user.listed_count
    favourites_count = user.favourites_count
    verified = prediction.encode_verified(user.verified)
    statuses_count = user.statuses_count
    default_profile = prediction.encode_default_profile(user.default_profile)
    default_profile_image = prediction.encode_default_profile_image(user.default_profile_image)
    has_extended_profile = prediction.encode_has_extended_profile(user.has_extended_profile)
    pred_list = [description, followers_count, friends_count, listed_count, favourites_count, verified, statuses_count, default_profile, default_profile_image, has_extended_profile, year, month, day, duration]
    pred_list = np.array(pred_list)
    #import model and predict
    pred_result = prediction.predict([pred_list])
    
    return render_template('bot_detection.html', user=user, pred_result = pred_result, registerform=registerform, modalshow=modalshow,loginform=loginform, loginmodalshow=loginmodalshow)

@twitter.route("/twitter/tweets/<string:name>")
@login_required
def user_tweets(name):
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
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    tweets = twitter_client.get_tweets_of_a_user(name, 3)
    length=dir(tweets[0])
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    tweets_likes_prediction =TweetLikesPrediction()
    sentences= df['text']
    likes = df['likes']
    
    return render_template('user_tweets.html', tweets=tweets,count=0, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)

