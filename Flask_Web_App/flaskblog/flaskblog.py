from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '959ffc08cc77d95dd1b22b7e67454823'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
db = SQLAlchemy(app)
