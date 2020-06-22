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
from code.algorithms import randomize as rd
from code.visualisation import visualise as vis
from code.algorithms import hillclimber as hc
from code.algorithms import depthfirst as df
from code.algorithms import breadthfirst as bf
import random
import csv

if __name__ == "__main__":

# ---------------User interface---------------------
    print("Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL \nContributors: Daphne Westerdijk, Lieke Kollen and Willem Henkelman\n")
    print("Welcome to our case RailNL, where we try to increase the efficiency and the quality of the rail network of the Netherlands. \nPlease press the button of the map that should be used:")
    map_size = input("1 : Holland\n2 : Netherlands\n")
    print("\nPlease select which algorithm you would like to use:")
    user_input = input("1 : Random\n2 : Random + Hill climber\n3 : Random greedy\n4 : Random greedy + Hill climber\n5 : Depth first\n6 : Depth first + Hill climber\n7 : Breadth first\n")
    
    repeats = int(input("How many times would you like to run the algorithm? We recommend running atleast x times for an accurate score."))
    
# ---------------Initializing map size---------------------
    if map_size == "1":
        stations_data_file = "data/StationsHolland.csv"
        connections_data_file = "data/ConnectiesHolland.csv"
        input_files = Map(stations_data_file, connections_data_file)
        duration = 120
        max_num_trajects = 7
        total_connections = 56
        start_stations = 3

    if map_size == "2":
        stations_data_file = "data/StationsNationaal.csv"
        connections_data_file = "data/ConnectiesNationaal.csv"
        input_files = Map(stations_data_file, connections_data_file)
        duration = 180
        max_num_trajects = 20
        total_connections = 178
        start_stations = 5

# ---------------Algoritms---------------------

    # ---------------Random--------------------
    if user_input == "1":
        
        random = rd.Random(input_files, duration, max_num_trajects, total_connections)
        random.run(repeats)
        print(f"Highscore: {random.highscore}, Duration: {random.complete_duration} Traject: {random.best_traject}")
        a_file = open("output/Randomscore.csv", "w", newline='')
        writer = csv.writer(a_file)
        for score in random.score_list:
            writer.writerow([score])
        a_file.close()
        vis.visualise(input_files, random.best_traject)

    # ---------------Random + Hill climber---------------------
    if user_input == "2":

        best_score = 0
        best_traject = None

        for i in range(repeats):
            
            input_files = Map(stations_data_file, connections_data_file)
            random = rd.Random(input_files,duration, max_num_trajects, total_connections)
            random.run(1)

            # ---------------Hill climber---------------------
            hillclimber = hc.HillClimber(random, input_files, total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")

    # ---------------Random greedy---------------------

    if user_input == "3":
       
        greedy = gr.Greedy(input_files, duration, max_num_trajects, total_connections)
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")
        greedy.run(repeats, min_max)
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

    if user_input == "4":
       
        print("This algorithm has a min and a max option. The min-option will prioritize the shortest possible connection and the max-option will prioritize the longest possible connection. ")
        min_max = input("Would you like to run min or max?:")

        best_score = 0
        best_traject = None

        for i in range(repeats):
            
            input_files = Map(stations_data_file, connections_data_file)
            greedy = gr.Greedy(input_files, duration, max_num_trajects, total_connections)
            greedy.run(1, min_max)

            # ---------------Hill climber---------------------
            hillclimber = hc.HillClimber(greedy, input_files, total_connections)
            hillclimber.run(100)
            print(f"iteration {i} = Highscore: {hillclimber.highscore}")

            if hillclimber.highscore > best_score:
                best_score = hillclimber.highscore
                best_traject = hillclimber.hillclimber_solution

        print(f"FINAL = Highscore: {best_score}, Traject: {best_traject}")
        
    # ---------------Depthfirst---------------------
    
    if user_input == "5":

        depth = df.Depthfirst(input_files, total_connections, start_stations)
        depth.run(repeats, duration)
        print(f"\nBest score: {depth.best_score} and solution: {depth.best_result}")

     # ---------------Depthfirst + Hill climber---------------------
    
    if user_input == "6":

        depth = df.Depthfirst(input_files, total_connections, start_stations)
        depth.run(repeats, duration)

        # ---------------Hill climber---------------------
    
    # ---------------Breadthfirst---------------------

    if user_input == "7":

        breadth = bf.Breadthfirst(input_files, total_connections, start_stations)
        breadth.run(repeats, duration)
        print(f"\nBest score: {breadth.best_score} and solution: {breadth.best_result}")