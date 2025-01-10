from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #disables CORs error, allows frontend and backend to communicate

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #local database location
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # does not track modifications made to database

db = SQLAlchemy(app) #instance of database


