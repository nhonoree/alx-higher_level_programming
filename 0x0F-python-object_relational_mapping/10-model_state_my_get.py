#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the engine and session
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state
    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
