#!/usr/bin/python3
"""
Module for the state table
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_mpre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id).all()

    for state in res:
        print(f"{state.id}: {state.name}")
    session.close()
