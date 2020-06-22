"""
 * helpers.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Supporting code for the main.py that handles the user interface and output
"""

import csv

class Helpers:
    """
    class that takes care of the user interface and creation of the output files 
    """

    def __init__(self):
        """
        
        """
        self.map_size = 1
        self.user_input = 1
        self.stations_data_file = "data/StationsHolland.csv"
        self.connections_data_file = "data/ConnectiesHolland.csv"
        self.duration = 0
        self.max_num_trajects = 0
        self.total_connections = 0
        self.repeats = 0
        self.start_stations = 0
        self.size = ""
        self.algorithm = ""

    def ask_input(self):
        print("Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL \nContributors: Daphne Westerdijk, Lieke Kollen and Willem Henkelman\n")
        print("Welcome to our case RailNL, where we try to increase the efficiency and the quality of the rail network of the Netherlands. \nPlease press the button of the map that should be used:")
        # assert self.map_size == 1 or self.map_size == 2
        self.map_size = input("1 : Holland\n2 : Netherlands\n")
        print("\nPlease select which algorithm you would like to use:")
        self.user_input = input("1 : Random\n2 : Random + Hill climber\n3 : Random greedy\n4 : Random greedy + Hill climber\n5 : Depth first\n6 : Depth first + Hill climber\n7 : Breadth first\n")
        
        self.repeats = int(input("How many times would you like to run the algorithm? We recommend running at least x times for an accurate score.\n"))
    
        if self.map_size == "1":
            self.stations_data_file = "data/StationsHolland.csv"
            self.connections_data_file = "data/ConnectiesHolland.csv"
            self.duration = 120
            self.max_num_trajects = 7
            self.total_connections = 56
            self.start_stations = 3
            

        elif self.map_size == "2":
            self.stations_data_file = "data/StationsNationaal.csv"
            self.connections_data_file = "data/ConnectiesNationaal.csv"
            self.duration = 180
            self.max_num_trajects = 20
            self.total_connections = 178
            self.start_stations = 5
    
    def combination(self, map_size, user_input):
        if map_size == "1":
            self.size = "Holland"
        
        elif map_size == "2":
            self.size = "Netherlands"
        
        if user_input == "1":
            self.algorithm = "random"
        
        elif user_input == "2":
            self.algorithm = "random-hillclimber"

        elif user_input == "3":
            self.algorithm = "greedy"

        elif user_input == "4":
            self.algorithm = "greedy-hillclimber"

        elif user_input == "5":
            self.algorithm = "depthfirst"
        
        return self.size and self.algorithm


    def output(self, score_list, map_size, user_input, best_traject, highscore):
        
        self.combination(map_size, user_input)
        
        a_file = open("output/{}/{}-scores.csv".format(self.size, self.algorithm), "w", newline='')
        writer = csv.writer(a_file)
        for score in score_list:
            writer.writerow([score])
        a_file.close()

        a_file = open("output/{}/{}-solution.csv".format(self.size, self.algorithm), "w", newline='')
        a_dict = best_traject
        writer = csv.writer(a_file)
        writer.writerow(['train', 'stations'])
        for key, value in a_dict.items():
            new = "[%s]" % (', '.join(value))
            writer.writerow([f'train_{key}', new])
        writer.writerow(['score', f'{highscore}'])
        a_file.close()
    
    # def cs50(self, best_traject, map_size, user_input, highscore):
    #     self.combination(map_size, user_input)
        