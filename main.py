from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algoritmes.greedy import *
import random

if __name__ == "__main__":
    stations_data_file = "data/StationsHolland.csv"
    connections_data_file = "data/ConnectiesHolland.csv"

    test = Map(stations_data_file, connections_data_file)
    #for station in test.stations:
        # print(test.stations[f'{station}'])
        #print(test.stations[f'{station}'].connections_list())

    new_traject = Traject(1, test.stations['Amsterdam Centraal'])


    while new_traject.total_distance < 300:
        current = new_traject.current_station

        new_traject.add_connection(random.choice(test.stations[f'{current}'].connections))
    greedy_start(new_traject)
