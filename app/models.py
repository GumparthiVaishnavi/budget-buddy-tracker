# Author: Your Name Here

# Developed by <your name>

from .db_config import db
from datetime import date

class ExpenseRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    recorded_on = db.Column(db.Date, default=date.today)

class BudgetPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64), nullable=False)
    month_key = db.Column(db.String(7), nullable=False)
    limit_amount = db.Column(db.Float, nullable=False)

class ProfileUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)

class SharedCircle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    circle_name = db.Column(db.String(64), nullable=False)
    users = db.relationship('ProfileUser', secondary='circle_members')

class CircleMember(db.Model):
    __tablename__ = 'circle_members'
    circle_id = db.Column(db.Integer, db.ForeignKey('shared_circle.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profile_user.id'), primary_key=True)