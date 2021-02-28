""" Geonames Class
Definition of the Geonames class with her attributes

@author: Mei, Lara & Sheherazade
"""
from flask import Flask,jsonify, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from . import db
from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float
import datetime


class Geonames(db.Model):
    """Geonames class
       Attributes:
    :param db: geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class 
    :param db: feature_code, country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code  
    :param db: population, elevation, dem, timezone, modification, modified_by
    """
    geonameid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    asciiname = db.Column(db.String(200), nullable=True)
    alternatenames = db.Column(db.String(10000), nullable=True)
    latitude = db.Column((db.Float), nullable=True)
    longitude = db.Column((db.Float), nullable=True)
    feature_class = db.Column(db.String(1), nullable=True)
    feature_code = db.Column(db.String(10), nullable=True)
    country_code = db.Column(db.String(2), nullable=True)
    cc2 = db.Column(db.String(200), nullable=True)
    admin1_code = db.Column(db.String(20), nullable=True)
    admin2_code = db.Column(db.String(80), nullable=True)
    admin3_code = db.Column(db.String(20), nullable=True)
    admin4_code = db.Column(db.String(20), nullable=True)
    population = db.Column((db.String), nullable=True)
    elevation = db.Column((db.String), nullable=True)
    dem = db.Column((db.String), nullable=True)
    timezone = db.Column(db.String(40), nullable=True)
    modification = db.Column((db.String), nullable=True)
    modified_by = db.Column((db.String), nullable=True)

  