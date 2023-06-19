#!/usr/bin/python3
""" prints the State object with the name passed
    as argument from the database.
    (SQL injection free)
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State) \
                    .filter(State.name == argv[4]).first()

    if states is None:
        print("Not Found")
    else:
        print('{}'.format(states.id))
