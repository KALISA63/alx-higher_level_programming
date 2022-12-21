#!/usr/bin/python3
"""
List all states matching given name from a MySQL db on localhost at port 3306
"""

from mysqlman import MySQLMan
from MySQLdb import Error
from sys import argv, exit, stderr


HELP = '{} username password database search'.format(argv[0])
HOST = 'localhost'
PORT = 3306


if __name__ == '__main__':
    try:
        params = {
            'user': argv[1],
            'password': argv[2],
            'database': argv[3],
            'host': HOST,
            'port': PORT,
        }
        search = argv[4]
    except IndexError:
        stderr.write('usage: {}\n'.format(HELP))
        exit(2)
    try:
        mysqlman = MySQLMan(connect=True, **params)
    except Error as e:
        stderr.write('{}\n'.format(e.args[1]))
        exit(1)
    query = """
    SELECT id, name
    FROM states
    WHERE BINARY name = %s
    ORDER BY id;
    """
    results = mysqlman.query([query, (search,)])
    for row in results[0]:
        print(row)
