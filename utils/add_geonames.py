""" module Creating Geonames DB
This module create the geonames table: bd.sqlite before to launch the service
input data: Fr.txt file recorded in the Data folder
output data: db.sqlite file database

@author: Mei, Lara & Sheherazade
"""

import sqlite3
import json
import re
from werkzeug.security import generate_password_hash
#insert new information to database
database = sqlite3.connect("../db.sqlite")
cursor = database.cursor()
# create database
def create_datase():
    """Create the database
    Attributes:
    :param db: geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class 
    :param db: feature_code, country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code  
    :param db: population, elevation, dem, timezone, modification, modified_by
    """
    # delete the table geonames if there is one
    sql_drop='''DROP TABLE IF EXISTS geonames'''

    # create the table geonames
    sql_create="""
    create table geonames (
        geonameid INT NOT NULL UNIQUE,
        name text NOT NULL,
        asciiname text ,
        alternatenames text,
        latitude Float,
        longitude Float,
        feature_class text,
        feature_code text,
        country_code text,
        cc2 char(2),
        admin1_code INT,
        admin2_code INT,
        admin3_code INT,
        admin4_code INT,
        population INT,
        elevation INT,
        dem INT,
        timezone text,
        modification date,
        modified_by text,
        PRIMARY KEY(geonameid)
        )
    """
    cursor.execute(sql_drop)
    cursor.execute(sql_create)
    
    
    
def insert_data():
    """Fill the database
    Attributes:
    :param db: geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class 
    :param db: feature_code, country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code  
    :param db: population, elevation, dem, timezone, modification, modified_by
    """
    with open("../data/FR.txt", "r",encoding="utf-8") as data:
        for l in data:
            l = re.sub(r" +", " ", l)
            if "," in l:
                l=l.replace(","," " )
            l=l.replace('\"',"\'" )
            line = l.split("\t")
            sql = f'INSERT INTO geonames (geonameid, name, asciiname, alternatenames,latitude,longitude,feature_class,feature_code,country_code,cc2,admin1_code,admin2_code,admin3_code,admin4_code,population,elevation,dem,timezone,modification) values ("{line[0]}","{line[1]}","{line[2]}","{line[3]}","{line[4]}","{line[5]}","{line[6]}","{line[7]}","{line[8]}","{line[9]}", "{line[10]}","{line[11]}","{line[12]}","{line[13]}","{line[14]}","{line[15]}", "{line[16]}","{line[17]}","{line[18]}");'
            cursor.execute(sql)
            database.commit()
    
    
    cursor.close()
    database.close()
    print("table geonames created!")
    

def main():
    create_datase()
    insert_data()

if __name__ == '__main__':
    main()







