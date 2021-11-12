from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid # unique key

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = str(uuid.uuid4())
db = SQLAlchemy(app)

from application import routes
