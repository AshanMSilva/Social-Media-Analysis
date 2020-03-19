from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer


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
	tweets = twitter_client.get_similar_tweets(hashtag, 'recent', 5)
	return render_template('hashtag.html', tweets=tweets)

@twitter.route("/twitter/<string:name>")
def user_details(name):
    twitter_client = TwitterClient()
    user = twitter_client.get_user(name)
    created_at = user.created_at
    id = user.id
    screen_name = user.screen_name
    description = user.description
    followers_count = user.followers_count
    friends_count = user.friends_count
    listed_count = user.listed_count
    favourites_count = user.favourites_count
    verified = user.verified
    statuses_count = user.statuses_count
    lang = user.lang
    default_profile = user.default_profile
    default_profile_image = user.default_profile_image
    name = user.name
    has_extended_profile = user.has_extended_profile


    
    return render_template('user_details.html', user=user)
