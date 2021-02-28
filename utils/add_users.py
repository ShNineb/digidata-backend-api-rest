""" module Creating the table Users added to the DB (bd.sqlite) once the client launched
File used automatically once the service launched
input data: user.json file recorded in the Data folder
output data: addes users to db.sqlite file database

@author: Mei, Lara & Sheherazade
"""

import sqlite3
import json
from werkzeug.security import generate_password_hash

class Add_users():
    def __init__(self,file_json):
        self.database = sqlite3.connect("./db.sqlite")
        self.cursor = self.database.cursor()
        self.create_datase()
        self.insert_data(file_json)

    # creer le tableau user
    def create_datase(self):
        """Create the table user in the database
        Attributes:
        :param db: id
        :param db: username
        :param db: password
        :param db: name
        """
        # delete the previous user table if existed
        sql_drop='''DROP TABLE IF EXISTS user'''
        
        # create  the user table
        sql_create='''
        create table if not exists user (
            id MEDIUMINT NOT NULL,
            username text NOT NULL UNIQUE,
            password text NOT NULL,
            name text,
            PRIMARY KEY(id)
            )
        '''
        # execute requests
        self.cursor.execute(sql_drop)
        self.cursor.execute(sql_create)
        
        
    # ajouter des données 
    def insert_data(self,file_json):
        """Fill the database
        Attributes:
        :param db: id
        :param db: username
        :param db: password
        :param db: name
        """ 
        with open(file_json, "r") as json_data:
            dicte_users = json.loads(json_data.read())
            for key in dicte_users.keys():
                id_user = int(key)
                username = dicte_users[key]["prenom"]+dicte_users[key]["nom"]
                username = username.lower()
                name = dicte_users[key]["prenom"]
                password = generate_password_hash(username+str(key),method='sha256')                
                self.cursor.execute(f"INSERT INTO user (id, username, name, password) values ('{id_user}', '{username}','{name}','{password}');")
                self.database.commit()
        # add data to the db
        self.cursor.close()
        self.database.close()
        print("Table user created!")
