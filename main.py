from code.classes.map import *

if __name__ == "__main__":
    stations_data_file = "data/StationsHolland.csv"
    connections_data_file = "data/ConnectiesHolland.csv"

    test = Map(stations_data_file, connections_data_file)
    for station in test.stations:
        print(test.stations[f'{station}'])    