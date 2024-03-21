"""
initialize the eduWeb package
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '972c87379d16a8a27665666e1cf17a35c44d39d4feddceda9d600c4d8b304436'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduweb.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


from eduWeb import routes