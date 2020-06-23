from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User


class Login(FlaskForm):
    user_name = StringField("User Name", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    uses_name = StringField("User Name", validators=[DataRequired(), Length(min=10, max=40)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=10, max=25)])
    password_confirm = PasswordField("Password Confirm", validators=[DataRequired(), Length(min=10, max=25), EqualTo('password')])
    full_name = StringField("Full Name", validators=[DataRequired(), Length(min=6, max=50)])
    submit = SubmitField("Register")

    def validate_user_name(self, user_name):
        user = User.objects(user_name=user_name.data).first()
        if user:
            raise ValidationError("User Name already in user. Please select a different one.")


class UserDetail(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    mobile_no = StringField("Mobile Number", validators=[DataRequired(), Length(min=10, max=13)])
    pan_number = StringField("Pan Card Number", validators=[DataRequired(), Length(min=10, max=11)])

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick anotherOr try to login  user. in.")


class UserFinancialDetails(FlaskForm):
    gross_salary = IntegerField("Gross Salary", validators=[DataRequired()])
    basic_salary = IntegerField("Basic Salary", validators=[DataRequired()])
    life_insurance_amount = IntegerField("Life Insaurance Amount", validators=[DataRequired()])
    home_loan_principal = IntegerField("Home Loan Principal Amount", validators=[DataRequired()])
    home_loan_interest = IntegerField("Home Loan Interest Rate", validators=[DataRequired()])
    PF = IntegerField("PF", validators=[DataRequired()])
    NPS = IntegerField("NPS", validators=[DataRequired()])
    HRA = IntegerField("HRA", validators=[DataRequired()])
    health_insurance = IntegerField("Health Insurance", validators=[DataRequired()])
    pension = IntegerField("Pension Plan Amount", validators=[DataRequired()])
    donation = IntegerField("Donation", validators=[DataRequired()])
