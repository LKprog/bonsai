from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algoritmes import greedy as gr
from code.algoritmes import random as rd
# from code.visualisation import visualise as vis
import random
import csv

if __name__ == "__main__":

    # type python main.py [number]
    # number = 1: random + National, 2: random + Holland, 3: greedy + National, 4: greedy + Holland

    from sys import argv

    if len(argv) != 2:
        print("Usage: python3 main.py [number]")
        exit(1)

    if argv[1] == '1':
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

        test = Map(stations_data_file, connections_data_file)

        # ---------------Random---------------------
        random = rd.Random(test,duration, max_num_trajects, lower_bound)
        random.run(5000)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        a_file = open("Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise(test, random.best_traject)
    
    if argv[1] == '2':
        stations_data_file = "data/StationsHolland.csv"
        connections_data_file = "data/ConnectiesHolland.csv"
        duration = 120
        max_num_trajects = 7
        lower_bound = 8460

        test = Map(stations_data_file, connections_data_file)

        # ---------------Random---------------------
        random = rd.Random(test,duration, max_num_trajects, lower_bound)
        random.run(5000)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        a_file = open("Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise(test, random.best_traject)
    
    if argv[1] == '3':
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

        test = Map(stations_data_file, connections_data_file)
        # ---------------Greedy---------------------
        greedy = gr.Greedy(test, duration, max_num_trajects, lower_bound)
        greedy.run(5000)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        a_file = open("Greedyscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in greedy.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise_all(test, greedy.best_traject)

    if argv[1] == '4':
        stations_data_file = "data/StationsHolland.csv"
        connections_data_file = "data/ConnectiesHolland.csv"
        duration = 120
        max_num_trajects = 7
        lower_bound = 8460

        test = Map(stations_data_file, connections_data_file)
        # ---------------Greedy---------------------
        greedy = gr.Greedy(test, duration, max_num_trajects, lower_bound)
        greedy.run(5000)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        a_file = open("Greedyscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in greedy.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise_all(test, greedy.best_traject)
    

    # # ---------------Greedy---------------------
    # greedy = gr.Greedy(test, duration, max_num_trajects, lower_bound)
    # greedy.run(1000)
    # print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

    # a_file = open("output.csv", "w", newline='')
    # a_dict = greedy.best_traject
    # writer = csv.writer(a_file)
    # writer.writerow(['train', 'stations'])
    # for key, value in a_dict.items():
    #     writer.writerow([f'train_{key}', f'{value}'])
    # writer.writerow(['score', f'{greedy.highscore}'])
    # a_file.close()

    # a_file = open("Greedyscore.csv", "w", newline='')
    # writer = csv.writer(a_file)
    # for score in greedy.score_list:
    #     writer.writerow([score])
    # a_file.close()
    # vis.visualise_all(test, greedy.best_traject)

    # ---------------Random---------------------
    # random = rd.Random(test,duration, max_num_trajects, lower_bound)
    # random.run(1000)
    # print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
    # a_file = open("Randomscore.csv", "w", newline='')
    # writer = csv.writer(a_file)
    # for score in random.score_list:
    #     writer.writerow([score])
    # a_file.close()
    # vis.visualise(test, random.best_traject)
