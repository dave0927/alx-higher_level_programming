#!/usr/bin/python3
"""Prints the State object with the name passed
    as argument"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    states = session.query(State) \
                    .filter(State.name == argv[4]).first()

    if states:
        print(states.id)
    else:
        print("Not Found")

    session.close()
