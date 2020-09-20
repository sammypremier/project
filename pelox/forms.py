from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), length(min=2, max=15)])
	email = StringField ('E-mail', validators=[DataRequired(), Email()])
	password = PasswordField ('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Become a model')


class LoginForm(FlaskForm):
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	login = SubmitField('Login')


