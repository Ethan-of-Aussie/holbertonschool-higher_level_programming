#!/usr/bin/python3
"""State class definition"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class linked to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nuulable=False, autoincrement=True)
    name =  Column(String(128), nullable=False)
