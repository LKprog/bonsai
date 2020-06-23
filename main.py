"""
 * main.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Main code of the RailNL case, .....
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
        Visual.visualise(input_files, random.best_traject, helper.score_csv)
        # Visual.histogram(helper.score_csv)

    # ---------------Random + Hill climber---------------------
    elif helper.user_algorithm == 2:

        # initialize variables
        best_score = 0
        best_traject = None

        for i in range(helper.repeats):
            
            # run the random algorithm once for each iteration
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            random = rd.Random(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            random.run(1)

            # ---------------Hill climber---------------------
            # run the hill climber for each iteration of the random algorithm
            hillclimber = hc.HillClimber(random, input_files, helper.total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")
            
            # compare the outcomes of the hill climber and save the best outcome
            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution
        
        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

        helper.output(hillclimber.score_list, helper.map_size, helper.user_input, best_traject, best_score)
        vis.visualise(input_files, best_traject)

    # ---------------Random greedy---------------------
    elif helper.user_algorithm == 3:
       
        # let the user select whether they want to have an algorithm using the shortest connections or the longest connections
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")

        # run the random greedy algorithm
        greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
        greedy.run(helper.repeats, min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")
        
        # create the output files: optimal solution and list of scores, and visualisation
        helper.output(greedy.score_list, helper.map_size, helper.user_algorithm, greedy.best_traject, greedy.highscore)
        vis.visualise(input_files, greedy.best_traject)
        # HISTOGRAMMM
    
    # ---------------Random greedy + Hill climber---------------------

    elif helper.user_algorithm == 4:
       
        # let the user select whether they want to have an algorithm using the shortest connections or the longest connections
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")

        # initialize variables
        best_score = 0
        best_traject = None

        for i in range(helper.repeats):
            
            # run the random greedy algorithm once for each iteration
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            greedy.run(1, min_max)

            # ---------------Hill climber---------------------
            # run the hill climber for each iteration of the random algorithm
            hillclimber = hc.HillClimber(greedy, input_files, helper.total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            # compare the outcomes of the hill climber and save the best outcome
            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

        helper.output(hillclimber.score_list, helper.map_size, helper.user_input, hillclimber.best_traject, hillclimber.best_score)
        vis.visualise(input_files, hillclimber.best_traject)
        
    # ---------------Depth first---------------------
    
    elif helper.user_algorithm == 5:
        
        # run the Depth first algorithm
        depth = df.Depthfirst(input_files, helper.total_connections, helper.start_stations)
        depth.run(helper.repeats, helper.duration)
        
        # helper.output(greedy.score_list, helper.map_size, helper.user_input, depth.best_result, depth.best_score)
        # vis.visualise(input_files, depth.best_result)

        print(f"\nBest score: {depth.best_score} and solution: {depth.best_result}")

    # ---------------Depth first + Hill climber---------------------
    
    elif helper.user_algorithm == 6:

        depth = df.Depthfirst(input_files, helper.total_connections, helper.start_stations)
        depth.run(helper.repeats, helper.duration)

        # ---------------Hill climber---------------------
    
    # ---------------Breadthfirst---------------------

    elif helper.user_algorithm == 7:

        breadth = bf.Breadthfirst(input_files, helper.total_connections, helper.start_stations)
        breadth.run(helper.repeats, helper.duration)
        print(f"\nBest score: {breadth.best_score} and solution: {breadth.best_result}")

