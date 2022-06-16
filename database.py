from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost/BD_Scraping"
api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(api)

class Telephone1(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    marque = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.String(255), nullable=False)
    # avis = db.Column(db.String(255), nullable=False)

class Telephone2(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    marque = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.String(255), nullable=False)
    # avis = db.Column(db.String(255), nullable=False)

class Telephone3(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # image = db.Column(db.String(255), nullable = False)
    marque = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.String(255), nullable=False)
    # avis = db.Column(db.String(255), nullable=False)

if __name__ == "__main__":
    db.drop_all()
    db.create_all()  
