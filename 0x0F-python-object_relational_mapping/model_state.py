#!/usr/bin/python3
'''
 contains the class definition of a State and an instance Base
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''    class definition inherits from Base    '''
    __tablename__ = 'states'

    id = Column("state_id", Integer, primary_key=True, nullable=False)
    name = Column("state_name", String(128), nullable=False)
