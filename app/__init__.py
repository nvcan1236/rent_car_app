from flask import Flask
from urllib.parse import quote
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import flask_admin
import sqlite3

app = Flask(__name__)
app.secret_key = 'DUKFHAKDGHNAK,DFHLDSKIFHALSK,JGDN ,KDFAJBN'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# login = LoginManager(app=app)
db = SQLAlchemy(app=app)
admin = flask_admin.Admin(app=app, template_mode='bootstrap4')
