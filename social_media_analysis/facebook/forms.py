from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,RadioField,TextAreaField,IntegerField,SelectField,validators
from wtforms.validators import DataRequired,ValidationError


class LikeForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    search = SubmitField('Predict')

class AdForm(FlaskForm):
    # name = StringField('Gender Targeted', validators=[DataRequired()])

    
    # name = StringField("Candidate Name ",[validators.Required("Please enter your name.")])  
    gender = RadioField('Gender Targeted', [validators.Required()],choices = [('M','Male'),('F','Female'),('A','All')],default='A')  
    adText  = TextAreaField("Ad Description",validators=[DataRequired()])  
    weekday = RadioField('week day', validators=[DataRequired()],choices = [('sun','Sunday'),('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday')],default='sun')
#   email = TextField("Email",[validators.Required("Please enter your email address."),  
#   validators.Email("Please enter your email address.")])       
    minAge = IntegerField("Minimum Age",validators=[DataRequired()])
    maxAge = IntegerField("Maximum Age",validators=[DataRequired()])  
    adSpends = IntegerField("Ad Spends in RUB",validators=[DataRequired()])
    # language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')]) 
    submit = SubmitField('Predict')

    def validate_age_range(self, minAge,maxAge):
        if (minAge>maxAge):
            raise ValidationError('That username is taken. Please choose a differ')

class SentiForm(FlaskForm):
    hashtag = StringField('Hash tag', validators=[DataRequired()])
    hashtagsubmit = SubmitField('Predict')