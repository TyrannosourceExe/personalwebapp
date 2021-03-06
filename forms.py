from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max =20)])
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	# allow users to stay logged on using a secure cookie
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')