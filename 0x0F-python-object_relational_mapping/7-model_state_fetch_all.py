#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check if we have enough arguments
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py mysql_username mysql_password db_name")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection string
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print the result
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
