#!/usr/bin/python3
"""
Provides a State class to map to objects in a states table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Defines a State class to map to objects in a states table
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    name = Column(
        String(128),
        nullable=False,
    )
