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

    # kiest een random startpunt

    for i in range(2):
        random_start = random.choice(list(test.stations))
        new_traject = Traject(i, test.stations[f'{random_start}'])

        while new_traject.traject_id < 8:
            current = new_traject.current_station
            random_connection = random.choice(test.stations[f'{current}'].connections)

            if random_connection[1] + new_traject.total_distance > 120:
                greedy_start(new_traject)
                break

            # als de random connectie niet al eerder is bezocht dan wordt hij aan het traject toegevoegd
            if random_connection[0] not in new_traject.trajects:
                new_traject.add_connection(random_connection)

        
