#!/usr/bin/python3
"""
Script link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    pre_ls = session.query(State, City)
    ls = pre_ls.filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in ls:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
