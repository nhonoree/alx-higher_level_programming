#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" in the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create engine and bind to the database
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}")
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add and commit to the database
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
