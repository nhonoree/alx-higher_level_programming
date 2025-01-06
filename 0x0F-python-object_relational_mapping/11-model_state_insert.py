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

    # Add a new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)
