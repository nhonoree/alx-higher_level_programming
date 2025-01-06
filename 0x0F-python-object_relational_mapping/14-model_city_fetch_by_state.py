# 14-model_city_fetch_by_state.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from state import State  # Assuming you have state.py and city.py in the same directory
from city import City

# Create an engine and connect to the MySQL database
engine = create_engine('mysql+mysqldb://root:password123@localhost/my_db', pool_pre_ping=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query to get all cities ordered by their ID
cities = session.query(City).order_by(City.id).all()

# Print the cities with their respective state
for city in cities:
    print(f"City: {city.name}, State: {city.state.name}")
