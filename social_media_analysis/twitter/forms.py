from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Screen Name', validators=[DataRequired()])
    search = SubmitField('Search')

class BotForm(FlaskForm):
    name = StringField('Screen Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class HashtagForm(FlaskForm):
    hashtag = StringField('Hash tag', validators=[DataRequired()])
    hashtagsubmit = SubmitField('Search')

class TweetForm(FlaskForm):
    name = StringField('Screen Name', validators=[DataRequired()])
    tweet = TextAreaField('Tweet', validators=[DataRequired()])
    #time = TimeField('Time (hh:mm)', validators=[DataRequired()])
    likespredict = SubmitField('predict')