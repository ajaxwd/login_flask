from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=128)])
    password = TextAreaField('Password', validators=[DataRequired(), Length(max=128)])
    Enviar = SubmitField('Enviar')
