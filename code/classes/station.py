"""
 * station.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Code for the station object that saves various properties such as x, y, all connections and unused connections
"""

class Station:
    """
    station class that loads the stations and its corresponding connections, it also tracks the station's unused connections
    """

    def __init__(self, name, x, y):
        """
        method to initialize the class and its properties
        """

        self.name = name
        self.x = x
        self.y = y
        self.connections = []
        self.unused_connections = []

    def connection(self, next_station, duration):
        """
        method to append the connection with name and duration to the stations connection list
        """

        self.connections.append([next_station, duration])

    def add_unused_connection(self, next_station, duration):
        """
        method to append the unused connections of the station to the unused connections list
        """

        self.unused_connections.append([next_station, duration])

    def __repr__(self):
        """
        method to make sure that the object is printed properly if it is in a list/dic
        """

        return self.name
