import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import MyInfo, Base, Resume, Contact
 
engine = create_engine('sqlite:///myportfolio.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


#my information like an about me
infoItem1 = MyInfo(
    name = "Austin Ridings",
    aboutme = "I am a Tier III Software Support Technician with newly acquired skills in Full Stack Software Engineering, I love building\
         new and exciting applications. My most recent Python project allows me to host my Resume and Portfolio as a Flask application\
         with an SQLite database. Currently I am actively learning and honing my development skills to transition into a full time Software Engineer.",
    skills = "Python, SQL, Bootstrap, Linux, AWS",
)

session.add(infoItem1)
session.commit()


#LRG employment info
jobItem1 = Resume(
    company = "Lowers Risk Group", 
    title = "Help Desk Technician - III", 
    location = "Purcellville, VA", 
    description = "A subject matter expert in all aspects of FuseOS and a FuseOS advocate within the company.\
        Provide prompt ongoing user support via Zendesk and user interactions, with a goal to meet an SLA of 2 hours for initial response.\
        Perform in-depth analysis of reported FuseOS issues using MySQL queries, Linux command line tool, regular expression log parsing\
        and issue verification in various FuseOS environments.\
        Support QA analysts in testing and documenting large enhancement features and releases, as needed.\
        Coach fellow Help Desk Agents in troubleshooting reported issues and managing user feedback", 
    dates = "Mar 01, 2019 - Present")

session.add(jobItem1)
session.commit()


jobItem2 = Resume(
    company = "Lowers Risk Group", 
    title = "Help Desk Technician - II", 
    location = "Purcellville, VA", 
    description = "Coordinated with Junior and Senior-level Developers to analyze and resolve FuseOS issues reported by users with\
        a goal to escalate less than 2%% of Help Desk tickets to a Developer for resolution.\
        Performed advanced level troubleshooting through the analysis of possible FuseOS defects.\
        Performed in-depth analysis of reported FuseOS issues using MySQL queries, Linux command line tool,\
        regular expression log parsing and issue verification in various FuseOS environments.", 
    dates = "Jan 01, 2018 - Mar 01, 2019")

session.add(jobItem2)
session.commit()


jobItem3 = Resume(
    company = "Lowers Risk Group", 
    title = "Help Desk Associate", 
    location = "Purcellville, VA", 
    description = "Subject matter expert in all aspects of FuseOS and a FuseOS advocate within the company.\
        Provide prompt ongoing user support via Zendesk and user interactions, with a goal to meet an SLA of 2 hours for initial response.\
        Contribute towards development and maintenance of content for Knowledge Base of FAQs and Known Issues to educate user community.", 
    dates = "Sept. 18, 2017 - Jan 01, 2018")

session.add(jobItem3)
session.commit()

#Contact information
contact1 = Contact(
    phone = "304-240-6583",
    email = "austinridings.dev@gmail.com",
)

session.add(contact1)
session.commit()


print("Data loaded to database!")