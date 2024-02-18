#!/usr/bin/python3
"""this lists the State object with the name passed as an arg
    from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    flag = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = True
            break
    if flag is False:
        print("Not found")
