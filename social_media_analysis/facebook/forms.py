from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class LikeForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    search = SubmitField('Predict')

class AdForm(FlaskForm):
    name = StringField('Screen Name', validators=[DataRequired()])
    submit = SubmitField('Predict')

class SentiForm(FlaskForm):
    hashtag = StringField('Hash tag', validators=[DataRequired()])
    hashtagsubmit = SubmitField('Predict')