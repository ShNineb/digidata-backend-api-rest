""" User Class
Definition of the User class with her attributes

@author: Mei, Lara & Sheherazade
"""

from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from . import db


class User(UserMixin,db.Model):
    """User class
       Attributes:
    :param db: id
    :param db: username
    :param db: password
    :param db: name
    """
    # attributes
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(200))

    def __repr__(self):
        return '<Name %r>' % self.id