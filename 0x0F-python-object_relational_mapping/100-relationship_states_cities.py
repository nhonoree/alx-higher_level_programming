#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py mysql_username mysql_password db_name")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)
    session.commit()

    session.close()

if __name__ == "__main__":
    main()
