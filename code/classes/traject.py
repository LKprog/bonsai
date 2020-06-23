"""
 * traject.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Code for the traject object which adds connections to the train route and keeps track of the duration 
 * and therefore represents a chain of connections
"""

from .station import Station

class Traject():
    """
    class that represents a train route comprised of multiple connections between Stations
    """
    def __init__(self, traject_id, current_station):
        """
        method that initializes the class for each route
        """
        self.traject_id = traject_id
        self.current_station = current_station
        self.trajects = []
        self.trajects.append(str(current_station))
        self.total_duration = 0

    def get_connection(self, current_station):
        """
        method that retrieves the possible connections for the current station in the traject
        """
        return self.current_station.connections_list

    def add_connection(self, next_station):
        """
        method that moves the current station of the traject to the next station and adds that station to the list of stations it has passed
        """
        self.trajects.append(next_station[0])
        self.total_duration += next_station[1]
        self.current_station = next_station[0]

    def __repr__(self):
        """
        method to make sure that the object is printed properly if it is in a list/dic
        """
        return str(self.trajects)
