from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    totalExpense = db.Column(db.Integer)
    expense = db.relationship('Expense')

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    expensename = db.Column(db.String(100))
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0)) 
    type = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))