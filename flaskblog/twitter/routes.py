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

