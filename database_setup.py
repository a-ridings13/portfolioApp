import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class MyInfo(Base):

    __tablename__ = 'myinformation'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class Resume(Base):

    __tablename__ = 'resume_data'

    company = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    title = Column(String(80), nullable = False)
    location = Column(String(250))
    description = Column(String(250))
    dates = Column(String(50))
    myinfo_id = Column(Integer, ForeignKey('myinformation.id'))
    myinformation = relationship(MyInfo)

#######insert at end of file#######

engine = create_engine('sqlite:///myportfolio.db')
Base.metadata.create_all(engine)