"""models"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users for analysis"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """Tweets pulled"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text= DB.Column(DB.Unicode(300))
    uid = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
