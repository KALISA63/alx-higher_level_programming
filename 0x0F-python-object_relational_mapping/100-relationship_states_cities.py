#!/usr/bin/python3
"""
Create the state California with the city San Francisco
"""

from relationship_state import Base, State
from relationship_city import City
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
    ca = State(name='California')
    sf = City(name='San Francisco')
    ca.cities.append(sf)
    session.add(ca)
    session.add(sf)
    session.commit()
    session.close()
