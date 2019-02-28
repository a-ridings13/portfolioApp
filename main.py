#!/usr/bin/env python
from flask import Flask, render_template, url_for, redirect, jsonify
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from database_setup import MyInfo, Base, Resume, Contact

app = Flask(__name__)

engine = create_engine('sqlite:///myportfolio.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/myportfolio")
def landingpage():
    info = session.query(MyInfo).order_by(asc(MyInfo.id))
    return render_template('main.html', info=info)

@app.route("/resume")
def myresume():
    items = session.query(Resume).order_by(asc(Resume.id))
    return render_template('resume.html', items=items)

@app.route("/contact")
def contactme():
    info = session.query(Contact).order_by(asc(Contact.id))
    return render_template('contact.html', info=info)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')