from flask_wtf import FlaskForm
from wtforms import SubmitField,FloatField, StringField,RadioField,TextAreaField,IntegerField,SelectField,validators,FileField
from wtforms.validators import DataRequired,ValidationError


class LikeForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    search = SubmitField('Predict')

class AdForm(FlaskForm):
    # name = StringField('Gender Targeted', validators=[DataRequired()])

    # name = StringField("Candidate Name ",[validators.Required("Please enter your name.")])  
    gender = RadioField('Gender Targeted', [validators.Required()],choices = [('M','Male'),('F','Female'),('A','All')],default='A')  
    adText  = TextAreaField("Ad Description",validators=[DataRequired("dis req")])  
    weekday = RadioField('week day', validators=[DataRequired()],choices = [('sun','Sunday'),('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday')],default='sun')
#   email = TextField("Email",[validators.Required("Please enter your email address."),  
#   validators.Email("Please enter your email address.")])       
    minAge = IntegerField("Minimum Age",validators=[DataRequired("Should be an integer !")])
    maxAge = IntegerField("Maximum Age",validators=[DataRequired("Should be an integer !")])  
    adSpends = FloatField("Ad Spends in USD",validators=[DataRequired("Should be an integer !")])
    # language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')]) 
    submit = SubmitField('Predict')

    def validate_maxAge(self,field):
        if(type(field.data)!=int):
            raise ValidationError("Should be an integer")
        if(field.data<=self.minAge.data):
        # if (minAge.data>self.maxAge.data):
            raise ValidationError("Invalid Age Range !!")
        if(field.data>65):
            raise ValidationError("Maximum age is 65 !!")

    def validate_minAge(self,field):
        if(type(field.data)!=int):
            raise ValidationError("Should be an integer")        
        if(field.data<13):
            raise ValidationError("Minimum age is 13 !!")
    def validate_adSpends(self,field):
        if( type(field.data)!=float):
            raise ValidationError("Should be a number")        
        if(field.data<0):
            raise ValidationError("Should be positive")


# class SentimentForm(FlaskForm):
#     upload=FileField("Upload your file here!",validators=[DataRequired()])
#     submit = SubmitField('Analyse')

class FbBotForm(FlaskForm):
    link=StringField('Profile Link :' ,validators=[DataRequired()])
    submit = SubmitField('Detect')