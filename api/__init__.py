import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # flask app
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{os.getcwd()}/todo.db"  # db location
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # tracking of modifications
db = SQLAlchemy(app)  # database