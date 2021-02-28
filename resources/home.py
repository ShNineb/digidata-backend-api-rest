""" Home Class
Home page

@author: Mei, Lara & Sheherazade
"""

from flask import Flask,jsonify, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

__all__ = ["Home"]


class Home(Resource):
    '''
    Returns
    -------
    Welcome message 
    '''
    def get(self):
        return ({'message' : 'Welcome to digidata!'})