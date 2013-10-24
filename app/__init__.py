from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Config parameters
SECRET_KEY = 'this is so secret?'
SQLALCHEMY_DATABASE_URI = 'sqlite:///app_db.sqlite'

app = Flask(__name__)
app.config.from_object(__name__)

# Intialize SQL Alchemy
db = SQLAlchemy(app)

import views