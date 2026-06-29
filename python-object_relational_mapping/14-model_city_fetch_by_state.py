#!/usr/bin/python3
""" prints all City objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    cities = session.query(
        City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: {(city.id)} {city.name}")
