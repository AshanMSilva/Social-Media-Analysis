from flask import render_template, url_for, flash, redirect, request, Blueprint,jsonify
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from social_media_analysis.stack_overflow import predict_maturity
import json
stack_overflow = Blueprint('stack_overflow', __name__)

@stack_overflow.route("/maturity", methods=["POST"])
def maturity():    
    data=request.form["userID"]
    dates=[] 
    barchartData={"languages": [ {"name": "Python", "percentage": 6.2}, {"name": "Ruby", "percentage": 3.3}, {"name": "HTML", "percentage": 2.2}, {"name": "CSS", "percentage": 0.7}, {"name": "Go", "percentage": 4.7}, {"name": "JavaScript", "percentage": 12.0}, {"name": "C#", "percentage": 7.2}, {"name": "C++", "percentage": 1.1}, {"name": "C", "percentage": 0.4}, {"name": "SQL", "percentage": 5.1}, {"name": "Scala", "percentage": 4.0}, {"name": "Clojure", "percentage": 0.4}, {"name": "Objective-C", "percentage": 0.4}], "web_frameworks": [{"name": "Reactjs", "percentage": 0.4}, {"name": "Express", "percentage": 0.4}, {"name": "Spring", "percentage": 1.1}], "other_frameworks": 0, "databases": [{"name": "Oracle", "percentage": 4.3}, {"name": "PostgreSQL", "percentage": 0.4}, {"name": "SQL-Server", "percentage": 0.7}], "platforms": [{"name": "MacOS", "percentage": 2.5}, {"name": "Windows", "percentage": 0.7}, {"name": "Linux", "percentage": 0.4}]}
    
    mat = predict_maturity.PredictMaturity(data)
    percentage = mat.get_user_maturity()
    dates = mat.get_percentage_list()
    barchartData=mat.get_user_technologies()
    dates=json.loads(dates)
    barchartData=json.loads(barchartData)
    

    return jsonify({"id":percentage,"dates":dates,"barchartData":barchartData})


