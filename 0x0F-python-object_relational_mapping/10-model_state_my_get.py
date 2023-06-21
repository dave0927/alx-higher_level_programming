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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}' \
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    name = argv[4]
    found = False
    states = session.query(State).order_by(State.id).all()

    for state in states:
        if state.name == name:
            print('{}'.format(states.id))
            found = True
            break
    
    if found is False:
        print("Not found")

    session.close()
