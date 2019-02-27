from flask import Flask, render_template, url_for
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from database_setup import MyInfo, Base, Resume

app = Flask(__name__)

engine = create_engine('sqlite:///myportfolio.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/myportfolio")
def landingpage():
    items = session.query(Resume).order_by(asc(Resume.id))
    return render_template('resume.html', items=items)

@app.route("/resume")
def myresume():
    return "this page will display my resume information"

@app.route("/contact")
def contactme():
    return "this page will display my contact information"




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')