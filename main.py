"""
 * main.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""
from helpers import Helpers
from code.classes.map import Map
from code.classes.station import Station
from code.classes.traject import Traject
from code.algorithms import random_greedy as gr
from code.algorithms import randomize as rd
from code.visualisation import visualise as vis
from code.algorithms import hillclimber as hc
from code.algorithms import depthfirst as df
from code.algorithms import breadthfirst as bf
import random
import csv

if __name__ == "__main__":

    helper = Helpers()
    helper.ask_input()
    
    input_files = Map(helper.stations_data_file, helper.connections_data_file)

# ---------------Algoritms---------------------

    # ---------------Random--------------------
    if helper.user_input == "1":
        
        random = rd.Random(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
        random.run(helper.repeats)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        a_file = open("output/Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        vis.visualise(input_files, random.best_traject)

    # ---------------Random + Hill climber---------------------
    elif helper.user_input == "2":

        best_score = 0
        best_traject = None

        for i in  range(helper.repeats):
            
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            random = rd.Randomize(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            random.run(1)

            # ---------------Hill climber---------------------
            hillclimber = hc.HillClimber(random, input_files, helper.total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

    # ---------------Random greedy---------------------

    elif helper.user_input == "3":
       
        greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")
        greedy.run(helper.repeats, min_max)
        print(f"Highscore: {greedy.highscore}, Duration: {greedy.complete_duration} Traject: {greedy.best_traject}")
        
        a_file = open("output.csv", "w", newline='')
        a_dict = greedy.best_traject
        writer = csv.writer(a_file)
        writer.writerow(['train', 'stations'])
        for key, value in a_dict.items():
            new = "[%s]" % (', '.join(value))
            writer.writerow([f'train_{key}', new])
        writer.writerow(['score', f'{greedy.highscore}'])
        a_file.close()

        a_file = open("output/Greedyscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in greedy.score_list:
            writer.writerow([score])
        a_file.close()
        vis.visualise(input_files, greedy.best_traject)
    
    # ---------------Random greedy + Hill climber---------------------

    elif helper.user_input == "4":
       
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")

        best_score = 0
        best_traject = None

        for i in range(helper.repeats):
            
            input_files = Map(helper.stations_data_file, helper.connections_data_file)
            greedy = gr.Greedy(input_files, helper.duration, helper.max_num_trajects, helper.total_connections)
            greedy.run(1, min_max)

            # ---------------Hill climber---------------------
            hillclimber = hc.HillClimber(greedy, input_files, helper.total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")
        
    # ---------------Depthfirst---------------------
    
    elif helper.user_input == "5":

        depth = df.Depthfirst(input_files, helper.total_connections, helper.start_stations)
        depth.run(helper.repeats, helper.duration)
        print(f"\nBest score: {depth.best_score} and solution: {depth.best_result}")

     # ---------------Depthfirst + Hill climber---------------------
    
    elif helper.user_input == "6":

        depth = df.Depthfirst(input_files, helper.total_connections, helper.start_stations)
        depth.run(helper.repeats, helper.duration)

        # ---------------Hill climber---------------------
    
    # ---------------Breadthfirst---------------------

    elif helper.user_input == "7":

        breadth = bf.Breadthfirst(input_files, helper.total_connections, helper.start_stations)
        breadth.run(helper.repeats, helper.duration)
        print(f"\nBest score: {breadth.best_score} and solution: {breadth.best_result}")
