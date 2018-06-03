# external
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
# internal


class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parolanız', validators=[DataRequired()])
    submit = SubmitField('Gönder')


class RegisterForm(FlaskForm):
    """ Kullanıcı kayıt formu"""
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parolanız', validators=[DataRequired()])
    submit = SubmitField('Kaydol')
