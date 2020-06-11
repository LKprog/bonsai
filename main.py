from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algoritmes import greedy as gr
from code.algoritmes import random as rd
import random

if __name__ == "__main__":
    stations_data_file = "data/StationsHolland.csv"
    connections_data_file = "data/ConnectiesHolland.csv"

    duration = 120
    max_num_trajects = 7

    test = Map(stations_data_file, connections_data_file)
    # station lijst
    # connectielijst
    # die meegeven aan de algoritmes

    # print(test.all_connections())
    # Trajecten konden niet worden aangemaakt in greedy.py dus dat moest wel hier
    traject_list = []
    i = 0
    while i < 7:
        start_station = random.choice(list(test.stations))
        new_traject = Traject(i, test.stations[f'{start_station}'])
        traject_list.append(new_traject)
        i += 1

    # # ---------------Greedy---------------------
    # greedy = gr.Greedy(test, traject_list, duration, max_num_trajects)
    # greedy.run()
    # print(f'{greedy.trajects}')


    # ---------------Random---------------------
    random = rd.Random(test, traject_list)
    
    random.run()
    print(f"Dict: {random.full_traject}, Num: {random.num_allstations}")
