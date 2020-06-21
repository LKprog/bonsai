"""
 * main.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""

from code.classes.map import Map
from code.classes.station import Station
from code.classes.traject import Traject
from code.algorithms import random_greedy as gr
from code.algorithms import random as rd
from code.visualisation import visualise as vis
from code.algorithms import hillclimber as hc
from code.algorithms import depthfirst as df
import random
import csv

if __name__ == "__main__":

    # type python main.py [number]
    # number = 1: random + National, 2: random + Holland, 3: greedy + National, 4: greedy + Holland

    print("Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL \n Contributors: Daphne Westerdijk, Lieke Kollen and Willem Henkelman")
    print("Algorithms:\nRandom : 1\nRandom_greedy : 2\nRandom/HillClimber : 3\nDepthfirst : 4")
    user_input = input("Please enter the number corresponding with the algorithm you would like to run:")
    size = input("Press 1 for Holland.\nPress 2 for the Netherlands.\n")
    repeats = int(input("How many times would you like to run the algorithm? We recommend running atleast x times for an accurate score."))
    if size == 1:
        stations_data_file = "data/StationsHolland.csv"
        connections_data_file = "data/ConnectiesHolland.csv"
        duration = 120
        max_num_trajects = 7
        lower_bound = 8460

    if size == 2:
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        duration = 180
        max_num_trajects = 20
        lower_bound = 4400

    if user_input == '1':

        test = Map(stations_data_file, connections_data_file)

        # ---------------Random---------------------
        random = rd.Random(test,duration, max_num_trajects, lower_bound)
        random.run(repeats)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        a_file = open("output/Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        vis.visualise(test, random.best_traject)

    if user_input == '2':

        test = Map(stations_data_file, connections_data_file)
        # ---------------Greedy---------------------
        greedy = gr.Greedy(test, duration, max_num_trajects, lower_bound)
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")
        greedy.run(repeats, min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        a_file = open("output/Greedyscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in greedy.score_list:
            writer.writerow([score])
        a_file.close()
        # vis.visualise_all(test, greedy.best_traject)

    if user_input == '3':
        best_score = 0
        best_traject = None

        i = 0
        while i < repeats:
            # ---------------Random---------------------
            test = Map(stations_data_file, connections_data_file)
            random = rd.Random(test,duration, max_num_trajects, lower_bound)
            random.run(1)
            print(f"Highscore: {random.highscore}, Duration: {random.complete_duration}")

            # ---------------HillClimber---------------------
            hillclimber = hc.HillClimber(random, test)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution
            i += 1
        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

    if user_input == '4':

        test = Map(stations_data_file, connections_data_file)
        # ---------------Depthfirst---------------------
        depth = df.Depthfirst(test)
        depth.run(duration, ['Den Helder', 'Maastricht'])
        print(f" best solution: {depth.ultimate_solution}")
