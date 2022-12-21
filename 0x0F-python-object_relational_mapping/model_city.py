#!/usr/bin/python3
"""
Provides a City class to map to objects in a cities table
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Defines a City class to map to objects in a cities table
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
    name = Column(
        String(256),
        nullable=False,
    )
