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
    cities = relationship('City', backref='state')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py mysql_username mysql_password db_name")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()

if __name__ == "__main__":
    main()
