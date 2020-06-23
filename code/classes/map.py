"""
 * map.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * This code loads all the stations and its connections and duration from the data files provided and it can be regarded as a literal map
 """

import csv
from .station import Station
from .traject import Traject

class Map:
    """
    class that functions as a 'map' in which the Station and Traject classes exist
    """

    def __init__(self, station_file, connection_file):
        """
        method that initializes the map, loads the stations objects and connections and makes a dict that contains all connections
        """

        self.stations = self.load_stations(station_file)
        self.connections = self.load_connections(connection_file)
        self.all_connections = {}

    def load_stations(self, source_file):
        """
        method that creates a Station object for each of the stations and its coordinates in the station_file
        """

        # create stations dict
        stations = {}

        # open the station_file
        with open(source_file, 'r') as input_file:

            # read the data per row and transfer it to the dict
            reader = csv.DictReader(input_file)
            for row in reader:
                station = Station(row['station'], float(row['x']), float(row['y']))
                stations[row['station']] = station

        return stations

    def load_connections(self, source_file):
        """
        method that creates connections for the stations object in both directions based on the connections_file
        """

        # open the connections_file and
        with open(source_file, 'r') as input_file:

            # read the data per row
            reader = csv.DictReader(input_file)
            for row in reader:

                # add the connection and duration to both the start station object and end station object of the connection, as a train can run both ways
                station = self.stations[row['station1']]
                station_reversed = self.stations[row['station2']]
                station.connection(row['station2'], int(float(row['distance'])))
                station_reversed.connection(row['station1'], int(float(row['distance'])))
                station.add_unused_connection(row['station2'], int(float(row['distance'])))
                station_reversed.add_unused_connection(row['station1'], int(float(row['distance'])))