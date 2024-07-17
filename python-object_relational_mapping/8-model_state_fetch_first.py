#!/usr/bin/python3
"""prints the first state object from database"""

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def list_state(user, passw, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db, pool_pre_ping=True))

    session = Session(engine)

    state = session.query(State).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print('Nothing')

    session.close()


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db = argv[3]

    list_state(user, password, db)
