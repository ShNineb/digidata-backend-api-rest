""" Logout Class
Manage the logout page

@author: Mei, Lara & Sheherazade
"""

from sqlalchemy import Float
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import datetime

__all__ = ["Logout"]

class Logout(Resource):
    @login_required
    def get(self):
        '''
        account logout 
        Returns
        -------
        A message to tell the account is logout

        '''
        logout_user()
        body = request.get_json()
        if 'username' in session:
            session.pop('username', None)
        return jsonify({'message' : 'You successfully logged out'})