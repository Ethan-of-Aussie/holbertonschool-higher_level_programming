#!/usr/bin/python3
"""prints the State object with
the name passed as argument from the database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()

    state = session.query(State).filter(state.name == sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
