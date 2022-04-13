#!/usr/bin/python3
'''
 contains the class definition of a City and an instance Base
'''
from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''    class definition inherits from Base    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
