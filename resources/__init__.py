from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
ma = Marshmallow()
db = SQLAlchemy()
from .home import *
from .logout import *
from .login import *
from .geo import *
from .user import User
from .geonames import Geonames
