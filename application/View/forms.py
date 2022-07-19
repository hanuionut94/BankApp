from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length, Email,EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=13)])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, max=13)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    user_id = StringField('CNP: ', validators=[DataRequired(), Length(min=13, max=13)])
    first_name = StringField('First name: ', validators=[DataRequired(), Length(min=5, max=30)])
    last_name = StringField('Last name: ', validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    address = StringField('Address: ', validators=[DataRequired(), Length(min=5, max=50)])
    phone_number = StringField('Phone number: ', validators=[DataRequired(), Length(min=10, max=10)])
    date_of_birth = StringField('Date of birth: ', validators=[DataRequired(), Length(min=5, max=30)])

    username = StringField('Username: ', validators=[DataRequired(), Length(min=6, max=13)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=6, max=13)])
    password = PasswordField('Confirm password: ', validators=[DataRequired(), Length(min=6, max=13), EqualTo('password')])

    submit = SubmitField('Register now!')
    
    # def validate_username(self, username):
    #     if UsersCredentials.query.filter_by(username=username).first():
    #         raise ValidationError('Username already in use.')

 