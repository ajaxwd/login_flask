from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(max=128)])
    password = StringField('Contraseña')
    submit = SubmitField('Enviar')
