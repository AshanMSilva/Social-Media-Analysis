from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
from flaskblog.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import numpy as np

facebook = Blueprint('facebook', __name__)
