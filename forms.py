from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField ,BooleanField
from wtforms.validators import DataRequired,Email ,EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField('username', validators = [DataRequired(),Length(min = 2 ,max =20)])
                                      
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    confirm_password = PasswordField('confirm password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Log in')