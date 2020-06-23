"""
 * helpers.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Supporting code for the main.py that handles the user interface and output
"""

import csv
from code.visualisation.visualise import Visual

class Helpers:
    """
    class that takes care of the user interface and creation of the output files
    """

    def __init__(self):
        """
        method to initialize the variables for the class Helpers and that are necessary to run main
        """
        self.map_size = 0
        self.user_algorithm = 0
        self.stations_data_file = ""
        self.connections_data_file = ""
        self.duration = 0
        self.max_num_trajects = 0
        self.total_connections = 0
        self.repeats = 0
        self.start_stations = 0
        self.size = ""
        self.algorithm = ""
        self.score_csv = ""

    def ask_input(self):
        """
        method to ask input from the user such as which region and which algorithm and sets values for the variables according to the choices
        """
        # Welcome the user to the case
        print("Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL \nContributors: Daphne Westerdijk, Lieke Kollen and Willem Henkelman\n")
        print("Welcome to our case RailNL, where we try to increase the efficiency and the quality of the rail network of the Netherlands.")

        # force the user to decide between the map of Holland or the Netherlands
        while True:
            print("Please press the button of the map that should be used:")
            self.map_size = int(input("1 : Holland\n2 : Netherlands\n"))
            if self.map_size != 1 and self.map_size != 2:
                print("Input not valid, try again")
            else:
                break

        # force the user to decide on an algorithm
        while True:
            print("\nPlease select which algorithm you would like to use:")
            self.user_algorithm = int(input("1 : Random\n2 : Random + Hill climber\n3 : Random greedy\n4 : Random greedy + Hill climber\n5 : Depth first\n6 : Breadth first\n"))
            if self.user_algorithm < 1 or self.user_algorithm > 7:
                print("Input not valid, try again")
            else:
                break

        # force the user to decide on the amount of times they want to run the algorithm
        while True:
            self.repeats = int(input("How many times would you like to run the algorithm? We recommend running at least x times for an accurate score.\n"))
            if not self.repeats:
                print("Input not valid, try again")
            else:
                break

        # depending on the choice for the map, set the values for the variables
        if self.map_size == 1:
            self.stations_data_file = "data/StationsHolland.csv"
            self.connections_data_file = "data/ConnectiesHolland.csv"
            self.duration = 120
            self.max_num_trajects = 7
            self.total_connections = 56
            self.start_stations = 3


        elif self.map_size == 2:
            self.stations_data_file = "data/StationsNationaal.csv"
            self.connections_data_file = "data/ConnectiesNationaal.csv"
            self.duration = 180
            self.max_num_trajects = 20
            self.total_connections = 178
            self.start_stations = 5

    def combination(self, map_size, user_algorithm):
        """
        method that translates the numbers of the variables map_size and user_algorithm to names
        """
        # translating the map_size
        if map_size == 1:
            self.size = "Holland"

        elif map_size == 2:
            self.size = "Netherlands"

        # translating the user_algorithm
        if user_algorithm == 1:
            self.algorithm = "random"

        elif user_algorithm == 2:
            self.algorithm = "random-hillclimber"

        elif user_algorithm == 3:
            self.algorithm = "greedy"

        elif user_algorithm == 4:
            self.algorithm = "greedy-hillclimber"

        elif user_algorithm == 5:
            self.algorithm = "depthfirst"

        elif user_algorithm == 6:
            self.algorithm = "breadthfirst"

        return self.size and self.algorithm

    def output(self, score_list, map_size, user_algorithm, best_traject, highscore):
        """
        method to create output files for all the scores and the best solution
        """
        # call the translating method
        self.combination(map_size, user_algorithm)

        # save the best solution in a csv file per map and algorithm
        a_file = open("output/{}/{}-solution.csv".format(self.size, self.algorithm), "w", newline='')
        a_dict = best_traject
        writer = csv.writer(a_file)
        writer.writerow(['train', 'stations'])
        for key, value in a_dict.items():
            new = "[%s]" % (', '.join(value))
            writer.writerow([f'train_{key}', new])
        writer.writerow(['score', f'{highscore}'])
        a_file.close()

        # save all the scores in a csv file per map and algorithm
        a_file = open("output/{}/{}-scores.csv".format(self.size, self.algorithm), "w", newline='')
        writer = csv.writer(a_file)
        for score in score_list:
            writer.writerow([score])
        a_file.close()

        self.score_csv = "output/{}/{}-scores.csv".format(self.size, self.algorithm)

        # overwrite the output.csv, can ben used for cs50
        a_file = open("output.csv", "w", newline='')
        a_dict = best_traject
        writer = csv.writer(a_file)
        writer.writerow(['train', 'stations'])
        for key, value in a_dict.items():
            new = "[%s]" % (', '.join(value))
            writer.writerow([f'train_{key}', new])
        writer.writerow(['score', f'{highscore}'])
        a_file.close()
