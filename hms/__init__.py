from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['Secret Key']='Secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
from hms import routes