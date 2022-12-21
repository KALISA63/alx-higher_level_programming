#!/usr/bin/python3
"""
Add the State object Louisiana to the states table of a MySQL database
"""

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, exit, stderr


HELP = '{} username password database'.format(argv[0])
HOST = 'localhost'
PORT = 3306
URLFORMAT = '{dialect}+{driver}://{user}:{password}@{host}/{database}'


if __name__ == '__main__':
    try:
        params = {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'user': argv[1],
            'password': argv[2],
            'host': HOST,
            'database': argv[3],
        }
    except IndexError:
        stderr.write('usage: {}\n'.format(HELP))
        exit(2)
    engine = create_engine(URLFORMAT.format(**params), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State).filter(City.state_id == State.id)
    for city, state in results.order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
