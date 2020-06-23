from application import app, db
from flask_sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # Personal Details
    user_name = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
    full_name = db.Column(db.String(50))
    pan_number = db.Column(db.String(10))
    mobile_number = db.Column(db.String(13))
    email = db.Column(db.String(50))
    # Location Details
    address = db.Column(db.String(120))
    city_name = db.Column(db.String(100))
    city_type = db.Column(db.String(10))
    # Taxable Required Field Details
    # Base Details
    gross_salary = db.Column(db.Integer)
    basic_salary = db.Column(db.Integer)
    life_insurance_amount = db.Column(db.Integer)
    home_loan_principal = db.Column(db.Integer)
    home_loan_interest = db.Column(db.Integer)
    PF = db.Column(db.Integer)
    NPS = db.Column(db.Integer)
    HRA = db.Column(db.Integer)
    health_insurance = db.Column(db.Integer)
    pension = db.Column(db.Integer)
    donation = db.Column(db.Integer)
    # Taxable Calculated Fields
    PF_amount = db.Column(db.Integer)
    HRA_amount = db.Column(db.Integer)
    NPS_amount = db.Column(db.Integer)
    home_loan_interest_amount = db.Column(db.Integer)
    _80C = db.Column(db.Integer)
    _80D = db.Column(db.Integer)
    _80CCD = db.Column(db.Integer)
    total_expenditure = db.Column(db.Integer)
    final_taxable_amount = db.Column(db.Integer)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)


