from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from social_media_analysis.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
from social_media_analysis.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import numpy as np

twitter = Blueprint('twitter', __name__)


@twitter.route("/twitter/<string:name>")
def user_details(name):
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    user = twitter_client.get_user(name)
    
    return render_template('user_details.html', user=user)



@twitter.route("/twitter/")
def hashtag_tweets():
	hashtag = request.args.get('hashtag')
	twitter_client = TwitterClient()
	tweets = twitter_client.get_similar_tweets(hashtag, 'recent', 1)
	return render_template('hashtag.html', tweets=tweets)

@twitter.route("/twitter/<string:name>")
def bot_account_detection(name):
    twitter_client = TwitterClient()
    user = twitter_client.get_user(name)
    prediction = Prediction()
    created_at = user.created_at
    year, month, day = prediction.get_date(created_at)
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
    pred_list = [description, followers_count, friends_count, listed_count, favourites_count, verified, statuses_count, default_profile, default_profile_image, has_extended_profile, year, month, day]
    pred_list = np.array(pred_list)
    #import model and predict
    pred_result = 0
    
    return render_template('bot_detection.html', user=user, pred_result = pred_result)
