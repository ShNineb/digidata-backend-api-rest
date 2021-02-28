""" Geo Class
Geo page creation with all his requets

@author: Mei, Lara & Sheherazade
"""

from flask import Flask,jsonify, request, session
from . import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_login import login_user, logout_user, login_required, LoginManager, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import datetime
from.geonames import Geonames
from .geonamesSchema import GeonamesSchema
geoname_schema = GeonamesSchema() 


class Geo(Resource):
    
    @login_required
    def get(self, geo_id):  
        """ Getting specific geo_id
        :param geo_id: geonameid (mandatory field)
        :return: information about this geoPoint if is in the DB else an error message
        """       
        geoname = Geonames.query.get(geo_id)
        if not geoname:
            abort(404, message="Could not find geopoint with that id.")
        return geoname_schema.jsonify(geoname)

    @login_required   
    def put(self, geo_id):
        """ Putting (adding) a specific geo_id
        :param geo_id: geonameid (mandatory field)
        :return: add informations about this new geoPoint if is in the DB an error message is given, else it's OK.
        """   

        # in case the geonameid is already present => add failed        
        result = Geonames.query.filter_by(geonameid=geo_id).first()
        if result:
            abort(404, message="Geo item already exist. ADD FAILED.")

        requestReceive = request.get_json()

        if requestReceive:

            if 'geonameid' in requestReceive:
                geonameid = request.json['geonameid']

                if str(geonameid) != str(geo_id): 
                    abort(404, message="geonameid in URL and Body do not match. Add FAILED.")

            else:
                abort(404, message="geonameid item is mandatory. Add FAILED.")        
          
            if 'name' in requestReceive:
                name = request.json['name']
            else:
                abort(404, message="name item is mandatory. Add FAILED.")   
                
            if 'asciiname' in requestReceive:
                asciiname = request.json['asciiname']
            else:
                asciiname =""

            if 'latitude' in requestReceive:
                latitude = request.json['latitude']
            else:
                latitude = None

            if 'longitude' in requestReceive:
                longitude = request.json['longitude']
            else:
                longitude = None

            if 'alternatenames' in requestReceive:
                alternatenames = request.json['alternatenames']
            else:
                alternatenames = ""            

            if 'feature_class' in requestReceive:
                feature_class = request.json['feature_class']
            else:
                feature_class =""

            if 'feature_code' in requestReceive:
                feature_code = request.json['feature_code']
            else:
                feature_code =""

            if 'country_code' in requestReceive:
                country_code = request.json['country_code']
            else:
                country_code= ""

            if 'cc2' in requestReceive:
                cc2 = request.json['cc2']
            else:
                cc2=""                

            if 'admin1_code' in requestReceive:
                admin1_code = request.json['admin1_code']
            else:
                admin1_code=""

            if 'admin2_code' in requestReceive:
                admin2_code = request.json['admin2_code']
            else:
                admin2_code=""

            if 'admin3_code' in requestReceive:
                admin3_code = request.json['admin3_code']
            else:
                admin3_code=""

            if 'admin4_code' in requestReceive:
                admin4_code = request.json['admin4_code']
            else:
                admin4_code="" 

            if 'population' in requestReceive:
                population = request.json['population']
            else:
                population=""

            if 'elevation' in requestReceive:
                elevation = request.json['elevation']
            else:
                elevation=""

            if 'dem' in requestReceive:
                dem = request.json['dem']
            else:
                dem="" 

            if 'timezone' in requestReceive:
                timezone = request.json['timezone']
            else:
                timezone=""

            if 'modification' in requestReceive:
                modification = request.json['modification']
            else:
                modification=""

            modified_by = current_user.username

        else:
            abort(404, message="No items input in Body. Add FAILED", details="geonameid and name are mandatory.")


    
        my_geopoints = Geonames(geonameid=geonameid, name=name, asciiname=asciiname, alternatenames=alternatenames, \
        latitude=latitude, longitude=longitude, feature_class=feature_class, feature_code=feature_code, \
        country_code=country_code, cc2=cc2, admin1_code=admin1_code, admin2_code=admin2_code, \
        admin3_code=admin3_code, admin4_code=admin4_code, population=population, elevation=elevation, \
        dem=dem, timezone=timezone, modification=modification, modified_by=modified_by)

        db.session.add(my_geopoints)
        db.session.commit()
    
        return geoname_schema.jsonify(my_geopoints)            


    @login_required
    def patch(self, geo_id):
        """ Updating a specific geo_id
        :param geo_id: geonameid (mandatory field)
        :return: update informations about this new geoPoint if is not in the DB an error message is given, else it's OK.
        """  
        geoname = Geonames.query.get(geo_id)

        jsonobjectDic = geoname_schema.dump(geoname)

        if not geoname:
            abort(404, message="Geo item doesn't exist. Update FAILED.")

        requestReceive = request.get_json()

        if requestReceive:

            if 'geonameid' in requestReceive:
                geoname.geonameid = request.json['geonameid']

                if str(geoname.geonameid) != str(geo_id):
                    abort(404, message="geonameid in URL and Body do not match. Update FAILED.")

            else:
                abort(404, message="geonameid item is mandatory. Update FAILED.")
            
            if 'name' in requestReceive:
                geoname.name = request.json['name']
            else:
                abort(404, message="name item is mandatory. Update FAILED.")
                
            if 'asciiname' in requestReceive:
                geoname.asciiname = request.json['asciiname']
            
            if 'alternatenames' in requestReceive:
                geoname.alternatenames = request.json['alternatenames']
            
            if 'latitude' in requestReceive:
                geoname.latitude = request.json['latitude']
            
            if 'longitude' in requestReceive:
                geoname.longitude = request.json['longitude']
            
            if 'feature_class' in requestReceive:
                geoname.feature_class = request.json['feature_class']
            
            if 'feature_code' in requestReceive:
                geoname.feature_code = request.json['feature_code']
            
            if 'country_code' in requestReceive:
                geoname.country_code = request.json['country_code']
            
            if 'cc2' in requestReceive:
                geoname.cc2 = request.json['cc2']
            
            if 'admin1_code' in requestReceive:
                geoname.admin1_code = request.json['admin1_code']
            
            if 'admin2_code' in requestReceive:
                geoname.admin2_code = request.json['admin2_code']
            
            if 'admin3_code' in requestReceive:
                geoname.admin3_code = request.json['admin3_code']
            
            if 'admin4_code' in requestReceive:
                geoname.admin4_code = request.json['admin4_code']
            
            if 'population' in requestReceive:
                geoname.population = request.json['population']
            
            if 'elevation' in requestReceive:
                geoname.elevation = request.json['elevation']
        
            if 'dem' in requestReceive:
                geoname.dem = request.json['dem']
            
            if 'timezone' in requestReceive:
                geoname.timezone = request.json['timezone']
            
            if 'modification' in requestReceive:
                geoname.modification = request.json['modification']
            
            geoname.modified_by = current_user.username

        else:
            abort(404, message="No items input in Body. Update FAILED", details="geonameid and name are mandatory.")

        db.session.commit()
        return geoname_schema.jsonify(geoname)

        
    
    @login_required
    def delete(self, geo_id):
        """ Deleting a specific geo_id
        :param geo_id: geonameid (mandatory field)
        :return: delete the geoPoint with all his informations. If is not in the DB an error message is given, else a confirmation is given.
        """  

        geoname = Geonames.query.get(geo_id)
        if not geoname:
            abort(404, message="Geo item doesn't exist. Delete FAILED.")
        db.session.delete(geoname)
        db.session.commit()

        return {'message':'Item deleted'}                
        
        