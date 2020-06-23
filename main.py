"""
 * main.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Main code of the RailNL case, running this will activate the user interface
"""

import random, csv
from helpers import Helpers
from code.classes.map import Map
from code.classes.station import Station
from code.classes.traject import Traject
from code.visualisation.visualise import Visual
from code.algorithms import randomize as rd, random_greedy as gr, hillclimber as hc, depthfirst as df, breadthfirst as bf

if __name__ == "__main__":

    # initialize the user interface
    helper = Helpers()
    helper.ask_input()
    vis = Visual()
    input_files = Map(helper.stations_data_file, helper.connections_data_file)

# ---------------Algoritms---------------------

    # ---------------Random--------------------
    if helper.user_algorithm == 1:

        # run the random algorithm
        random = rd.Random(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
        random.run(helper.repeats)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")

        # create the output files: optimal solution and list of scores, and visualisation
        helper.output(random.score_list, helper.map_size, helper.user_algorithm, random.best_traject, random.highscore)
        vis.visualise(input_files, random.best_traject, helper.score_csv)


    # ---------------Random + Hill climber---------------------
    elif helper.user_algorithm == 2:

        # initialize variables
        best_score = 0
        best_traject = None
        score_list = []

        for i in range(helper.repeats):
            if i%10 == 0:
                print(f"{i}/{helper.repeats}")

            # run the random algorithm once for each iteration
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            random = rd.Random(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            random.run(1)

            # ---------------Hill climber---------------------
            # run the hill climber for each iteration of the random algorithm
            hillclimber = hc.HillClimber(random, input_files, helper.total_connections)
            hillclimber.run(100)

            # compare the outcomes of the hill climber and save the best outcome
            score_list.append(hillclimber.highscore)
            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

        helper.output(score_list, helper.map_size, helper.user_algorithm, best_traject, best_score)
        vis.visualise(input_files, best_traject, helper.score_csv)

    # ---------------Random greedy---------------------
    elif helper.user_algorithm == 3:

        # let the user select whether they want to have an algorithm using the shortest connections or the longest connections
        helper.ask_greedy()

        # run the random greedy algorithm
        greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
        greedy.run(helper.repeats, helper.min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")

        # create the output files: optimal solution and list of scores, and visualisation
        helper.output(greedy.score_list, helper.map_size, helper.user_algorithm, greedy.best_traject, greedy.highscore)
        vis.visualise(input_files, greedy.best_traject, helper.score_csv)

    # ---------------Random greedy + Hill climber---------------------
    elif helper.user_algorithm == 4:

        # let the user select whether they want to have an algorithm using the shortest connections or the longest connections
        helper.ask_greedy()

        # initialize variables
        best_score = 0
        best_traject = None
        score_list = []

        for i in range(helper.repeats):
            if i%10 == 0:
                print(f"{i}/{helper.repeats}")

            # run the random greedy algorithm once for each iteration
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            greedy.run(1, helper.min_max)

            # ---------------Hill climber---------------------
            # run the hill climber for each iteration of the random algorithm
            hillclimber = hc.HillClimber(greedy, input_files, helper.total_connections)
            hillclimber.run(100)

            # compare the outcomes of the hill climber and save the best outcome
            score_list.append(hillclimber.highscore)
            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

        helper.output(score_list, helper.map_size, helper.user_algorithm, best_traject, best_score)
        vis.visualise(input_files, best_traject, helper.score_csv)

    # ---------------Depth first---------------------
    elif helper.user_algorithm == 5:

        # run the Depth first algorithm
        depth = df.Depthfirst(input_files, helper.total_connections, helper.start_stations)
        depth.run(helper.repeats, helper.duration)

        helper.output(depth.score_list, helper.map_size, helper.user_algorithm, depth.best_result, depth.best_score)
        print(f"\nBest score: {depth.best_score} and solution: {depth.best_result}")
        vis.visualise(input_files, depth.best_result, helper.score_csv)


    # ---------------Breadthfirst---------------------
    elif helper.user_algorithm == 6:
        # run the Breadth first algorithm
        breadth = bf.Breadthfirst(input_files, helper.total_connections, helper.start_stations)
        breadth.run(helper.repeats, helper.duration)

        helper.output(breadth.score_list, helper.map_size, helper.user_algorithm, breadth.best_result, breadth.best_score)
        print(f"\nBest score: {breadth.best_score} and solution: {breadth.best_result}")
        vis.visualise(input_files, breadth.best_result, helper.score_csv)
