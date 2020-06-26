from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,SelectField
from wtforms.validators import DataRequired


class ChannelDetailForm(FlaskForm):
    name = StringField('Channel ID', validators=[DataRequired()])
    search = SubmitField('Search')

class SentimentAnalysisForm(FlaskForm):
    name = StringField('Video ID', validators=[DataRequired()])
    searchSent = SubmitField('Search')
    

class ViewPredictionForm(FlaskForm):
    
    values=[("","---"),("1","Film & Animation"),("2","Autos & Vehicles"),("10","Music"),("15","Pets & Animals"),("17","Sports"),("18","Short Movies"),
            ("19","Travel & Events"),("20","Gaming"),("21","Videoblogging"),("22","People & Blogs"),("23","Comedy"),("24","Entertainment"),("25","News & Politics"),
            ("26","Howto & Style"),("27","Education"),("28","Science & Technology"),("29","Nonprofits & Activism"),("30","Movies")]
    channel = StringField('Channel ID', validators=[DataRequired()])
    #category = StringField('Category ID', validators=[DataRequired()])
    category = SelectField('Category', choices =  values, validators=[DataRequired()],validate_choice=False)
    length = StringField('Video Length (in seconds)', validators=[DataRequired()])
    viewspredict = SubmitField('Predict')
    
    
class ViralVideoForm(FlaskForm):
    searchView = SubmitField('View')