from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField,TimeField,SelectField
from wtforms.validators import DataRequired


class ChannelDetailForm(FlaskForm):
    name = StringField('Channel ID', validators=[DataRequired()])
    search = SubmitField('Search')

class SentimentAnalysisForm(FlaskForm):
    name = StringField('Video ID', validators=[DataRequired()])
    searchSent = SubmitField('Search')
    

class ViewPredictionForm(FlaskForm):
    #values=[("1","1-Film & Animation"),2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,(30,"Movies")]
    values=[("","---"),("1","Film & Animation"),("2","Movies")]
    channel = StringField('Channel ID', validators=[DataRequired()])
    category = StringField('Category ID', validators=[DataRequired()])
    category = SelectField('Category ID', choices =  values, validators=[DataRequired()],validate_choice=False)
    length = StringField('Video Length (in seconds)', validators=[DataRequired()])
    viewspredict = SubmitField('predict')
    
    
class ViralVideoForm(FlaskForm):
    searchView = SubmitField('View')