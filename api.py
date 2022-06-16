from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from database import *
from flask import Flask, flash, jsonify, redirect, request, render_template



api = Flask(__name__)

api.config['SECRET_KEY'] = 'groupe4'
api.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost/BD_Scraping"
api.config['CORS_HEADERS'] = 'Content-Type'
api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api.config["JSON_SORT_KEYS"] = False






@api.route('/')
def telIphone():
    produit = Telephone1.query.order_by(desc(Telephone1.prix))
    produit2 = Telephone2.query.order_by(desc(Telephone2.prix))
    produit3 = Telephone3.query.order_by(desc(Telephone3.prix))

    return render_template ('donneIphone.html',produit = produit, produit2 = produit2, produit3 = produit3)


@api.route('/dashbord')
def dashbord():
    donne_tel1= Telephone1.query.all()
    phone=Telephone2.query.all()
    dataPhone = Telephone3.query.all()
    list_datas=[]
    phones = []
    iphone = []
    dataPhones =[]
    for don in donne_tel1:
        v=(don.marque)
        u =(don.prix)
        list_datas.append([v,u])
    for tel in phone:
        k =(tel.marque)
        l = (tel.prix)
        phones.append([k,l])
    for tele in dataPhone:
        m = (tele.marque)
        n = (tele.prix)
        dataPhones.append([m,n])
    return render_template('dashbord.html',list_datas = list_datas, phones = phones, dataPhones = dataPhones)




db.init_app(api)
api.run(host="localhost", port=8000, debug=True)




