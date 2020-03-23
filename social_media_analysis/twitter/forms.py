from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class screenNameForm(FlaskForm):
    name = TextAreaField('Screen Name', validators=[DataRequired()])
    submit = SubmitField('Search')