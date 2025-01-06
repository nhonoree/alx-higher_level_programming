#!/usr/bin/python3
"""
Defines the State class with a relationship to the City class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with the City class
    cities = relationship('City', backref='state', cascade='all, delete')
