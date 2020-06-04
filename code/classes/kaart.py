import csv
from .station import Station

class Kaart():
    def __init__(self, station_file):
        self.stations = self.load_stations(station_file)
        # self.connections = self.load_connections(connection_file)

    def load_stations(self, source_file):
        stations = {}
        with open(source_file, 'r') as input_file:
            reader = csv.DictReader(input_file)
            
            for row in reader:
                station = Station(row['station'], row['x'], row['y'])
                stations[row['station']] = station

        return stations

    # def load_connections(self, source_file):
    #     with open(source_file, 'r') as input_file:
    #         reader = csv.DictReader(input_file)
            
    #         for row in reader:
    #             station = self.stations[row['station1']]

