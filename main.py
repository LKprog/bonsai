from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algoritmes import greedy as gr
import random

if __name__ == "__main__":
    stations_data_file = "data/StationsHolland.csv"
    connections_data_file = "data/ConnectiesHolland.csv"

    test = Map(stations_data_file, connections_data_file)

    # Trajecten konden niet worden aangemaakt in greedy.py dus dat moest wel hier
    traject_list = []
    i = 0
    while i < 1:
        start_station = random.choice(list(test.stations))
        new_traject = Traject(i, test.stations[f'{start_station}'])
        traject_list.append(new_traject)
        i += 1

    #for station in test.stations:
        # print(test.stations[f'{station}'])
        #print(test.stations[f'{station}'].connections_list())

    # # kiest een random startpunt
    # traject_list = []
    # stations_list = []
    # i = 0
    # while i < 7:

    #     start_station = random.choice(list(test.stations))
    #     new_traject = Traject(i, test.stations[f'{start_station}'])

    #     while True:
    #         current = new_traject.current_station
    #         #if current not in stations_list:
    #             #stations_list.append(current)
    #         #if len(stations_list) == 28:
    #             #print('break1')
    #             #break
    #         random_connection = random.choice(test.stations[f'{current}'].connections)

    #         if random_connection[1] + new_traject.total_distance > 120:
    #             traject_list.append(new_traject)
    #             i += 1

    #             greedy_start(new_traject)
    #             break

    #         # als de random connectie niet al eerder is bezocht dan wordt hij aan het traject toegevoegd
    #         if random_connection[0] not in new_traject.trajects:
    #             new_traject.add_connection(random_connection)

    #         else:
    #             break
    #     #if len(stations_list) == 28:
    #         #print('break2')
    #         #print(stations_list)
    #         #break

    greedy = gr.Greedy(test, traject_list)
    greedy.run()
    print(f'{greedy.trajects}')