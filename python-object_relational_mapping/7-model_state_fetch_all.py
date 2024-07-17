#!/usr/bin/python3
"""script that lists all state objects from database"""

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def list_state(user, passw, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db, pool_pre_ping=True))

    session = Session(engine)

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    list_state(user, passwd, database)
