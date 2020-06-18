from code.classes.map import *
from code.classes.station import *
from code.classes.traject import *
from code.algorithms import random_greedy as gr
from code.algorithms import random as rd
# from code.visualisation import visualise as vis
from code.algorithms import hillclimber as hc
from code.algorithms import depthfirst as df
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
        random.run(1)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        # a_file = open("output/Randomscore.csv", "w", newline='')
        # writer = csv.writer(a_file)
        # for score in random.score_list:
        #     writer.writerow([score])
        # a_file.close()
        vis.visualise(test, random.best_traject)

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
        a_file = open("output/Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        vis.visualise(test, random.best_traject)

    if argv[1] == '3':
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

        test = Map(stations_data_file, connections_data_file)
        # ---------------Greedy---------------------
        greedy = gr.Greedy(test, duration, max_num_trajects, lower_bound)
        min_max = input("Min or max?:")
        greedy.run(1000, min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        a_file = open("output/Greedyscore.csv", "w", newline='')
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
        min_max = input("Min or max?:")
        greedy.run(1000, min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        a_file = open("output/Greedyscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in greedy.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise_all(test, greedy.best_traject)

    if argv[1] == '5':
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

        test = Map(stations_data_file, connections_data_file)

        # ---------------Random---------------------
        random = rd.Random(test,duration, max_num_trajects, lower_bound)
        random.run(100000)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")

        # ---------------HillClimber---------------------
        hillclimber = hc.HillClimber(random, test)
        hillclimber.run(10000)
        print(f"Highscore: {hillclimber.highscore}, Traject: {hillclimber.hillclimber_solution}")

    if argv[1] == '6':
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

        test = Map(stations_data_file, connections_data_file)
        # ---------------Depthfirst---------------------
        depth = df.Depthfirst(test)
        depth.run(duration, ['Den Helder', 'Maastricht'])
        print(f" best solution: {depth.ultimate_solution}")
