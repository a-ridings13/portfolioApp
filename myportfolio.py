import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import MyInfo, Base, Resume
 
engine = create_engine('sqlite:///myportfolio.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()



#LRG employment info
jobItem1 = Resume(company = "Lowers Risk Group", title = "Help Desk Technician - III", location = "Purcellville, VA", description = "", dates = "Mar 01, 2019 - Present")

session.add(jobItem1)
session.commit()


jobItem2 = Resume(company = "Lowers Risk Group", title = "Help Desk Technician - II", location = "Purcellville, VA", description = "", dates = "Jan 01, 2018 - Mar 01, 2019")

session.add(jobItem2)
session.commit()


jobItem3 = Resume(company = "Lowers Risk Group", title = "Help Desk Associate", location = "Purcellville, VA", description = "", dates = "Sept. 18, 2017 - Jan 01, 2018")

session.add(jobItem3)
session.commit()


print("Resume loaded to database!")