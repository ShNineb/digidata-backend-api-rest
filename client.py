""" Client - main program
Creation of an API Rest using Ptyhon Flask, FlaskRestful, MArshmallow For the backen build application.
Tests of the backend solution made through Postman.

@author: Mei, Lara & Sheherazade
"""

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify, request, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Float
import datetime
import resources 
import utils


# generate the user table (geo table is already done
# cf. documentation forr more information on howToGenerate it.)
users_file = "./data/users.json"
utils.Add_users(users_file)

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
#loading the database created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SERVER_NAME'] = 'digidata.api.localhost'


resources.db.init_app(app)
#create object of Marshmallow
ma = Marshmallow(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """ Method to return userid
    :return:  user_id    
    """
    return resources.User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    """ Method to try if logged
    :return:  message if non authorized    
    """
    return jsonify({'info' : 'Log-in required for this request.'})

# routes for each methods from there page
api.add_resource(resources.Home, "/", "/home")
api.add_resource(resources.Login, "/login")
api.add_resource(resources.Logout, "/logout")
api.add_resource(resources.Geo, "/geo/<int:geo_id>")


if __name__ == "__main__":
    
    app.run(debug=True,host='localhost',port='5000')