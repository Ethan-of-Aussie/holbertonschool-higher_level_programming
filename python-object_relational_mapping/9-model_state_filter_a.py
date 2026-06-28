#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' in their name."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name.lower():
            print(f"{state.id}: {state.name}")
    session.close()
