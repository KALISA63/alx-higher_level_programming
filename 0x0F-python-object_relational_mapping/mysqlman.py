"""
Provides a class to manage MySQL database connections and queries
"""

from MySQLdb import connect


class MySQLMan():
    """
    Manages a connection to a MySQL database
    """
    def __init__(self, connect=False, **kwargs):
        """
        Instantiate a MySQLMan object
        """
        if type(connect) is not bool:
            raise TypeError("'connect' must be of type 'bool'")
        self.__connection = None
        self.__cursor = None
        self.__params = kwargs
        if connect:
            self.connect()

    @property
    def connection(self):
        """
        Get the value of the private instance attribute 'connection'
        """
        return self.__connection

    @connection.deleter
    def connection(self):
        """
        Close an active connection upon object deletion
        """
        self.disconnect()

    @property
    def connected(self):
        """
        Check for an active connection
        """
        return self.connection is not None and not self.connection.closed

    def connect(self, **kwargs):
        """
        Open a connection
        """
        if self.connected:
            raise RuntimeError("Connection already established")
        params = self.__params
        params.update(kwargs)
        self.__connection = connect(**params)
        self.__cursor = self.connection.cursor()

    def disconnect(self):
        """
        Close a connection
        """
        if self.connected():
            self.connection.close()
        self.__connection = None
        self.__cursor = None

    def reconnect(self, **params):
        """
        Close and reopen a connection
        """
        self.disconnect()
        self.connect()

    def query(self, *args):
        """
        Query a database
        """
        results = []
        for query, values in args:
            self.__cursor.execute(query, values)
            results.append(self.__cursor.fetchall())
        return results
