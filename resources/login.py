""" Login Class
Manage the login page

@author: Mei, Lara & Sheherazade
"""


from . import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .user import User


class Login(Resource):
    """A Login class for users"""
    # la requête get
    def get(self):
        '''
        Returns
        -------
        un message accueil

        '''
        return ({'message' : 'Welcome to digidata'}) , 200
    
    # la requête post
    def post(self):
        '''
        Collect the username and the user password
        Returns
        -------
        If the account has access: a welcome message otherwise an error message
        '''
        body = request.get_json()
        user = User.query.filter_by(username=body.get('username')).first()
        if not user or not check_password_hash(user.password, body.get('password')):
            return {'error': 'username or password invalid'}, 401
        
        login_user(user)
        return ({'message' : 'Welcome! You are logged in.'}), 201