import csv
from .station import Station
from .traject import Traject

class Map():
    """
    class that functions as a 'map' in which the Station- and Traject-classes exist
    """
    def __init__(self, station_file, connection_file):
        self.stations = self.load_stations(station_file)
        self.connections = self.load_connections(connection_file)
        self.all_connections = {}

    def load_stations(self, source_file):
        """
        method that creates a Station object for each of the stations in a csv file
        """
        stations = {}
        with open(source_file, 'r') as input_file:
            reader = csv.DictReader(input_file)

            for row in reader:
                station = Station(row['station'], float(row['x']), float(row['y']))
                stations[row['station']] = station

        return stations

    def load_connections(self, source_file):
        """
        method that creates connections between Stations
        """
        with open(source_file, 'r') as input_file:
            reader = csv.DictReader(input_file)

            for row in reader:
                station = self.stations[row['station1']]
                station_reversed = self.stations[row['station2']]
                station.connection(row['station2'], int(float(row['distance'])))
                station_reversed.connection(row['station1'], int(float(row['distance'])))
                station.add_unused_connection(row['station2'], int(float(row['distance'])))
                station_reversed.add_unused_connection(row['station1'], int(float(row['distance'])))

    def all_connections(self):
        """
        method that returns a list of al of the possible connections between Stations
        """

        for stad in self.stations:
            all_connections[stad] = []

            for connection in self.stations[stad].connections:
               all_connections[stad].append(connection)

        return all_connections
