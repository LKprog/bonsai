from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algoritmes import greedy as gr
from code.algoritmes import random as rd
from code.visualisation import visualise as vis
import random

if __name__ == "__main__":
    stations_data_file = "data/StationsHolland.csv"
    connections_data_file = "data/ConnectiesHolland.csv"

    duration = 120
    max_num_trajects = 7

    test = Map(stations_data_file, connections_data_file)

    # # ---------------Greedy---------------------
    # greedy = gr.Greedy(test, traject_list, duration, max_num_trajects)
    # greedy.run()
    # print(f'{greedy.trajects}')


    # ---------------Random---------------------
    random = rd.Random(test,duration, max_num_trajects)
    random.run(100)
    # random.coordinates(random.best_traject)
    print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
    vis.visualise_all(test, random.best_traject)
