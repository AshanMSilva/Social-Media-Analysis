from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,RadioField,TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired


class LikeForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    search = SubmitField('Predict')

class AdForm(FlaskForm):
    # name = StringField('Gender Targeted', validators=[DataRequired()])

    
    # name = StringField("Candidate Name ",[validators.Required("Please enter your name.")])  
    gender = RadioField('Gender Targeted', choices = [('M','Male'),('F','Female'),('A','All')])  
    adText  = TextAreaField("Ad Description")  
    weekday = RadioField('week day', choices = [('sun','Sunday'),('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday')])
#   email = TextField("Email",[validators.Required("Please enter your email address."),  
#   validators.Email("Please enter your email address.")])       
    minAge = IntegerField("Minimum Age")
    maxAge = IntegerField("Maximum Age")  
    adSpends = IntegerField("Ad Spends in RUB")
    # language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')]) 
    submit = SubmitField('Predict')

class SentiForm(FlaskForm):
    hashtag = StringField('Hash tag', validators=[DataRequired()])
    hashtagsubmit = SubmitField('Predict')