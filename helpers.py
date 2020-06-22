class Helpers:

    def __init__(self):
        self.map_size = 1
        self.user_input = 1
        self.stations_data_file = "data/StationsHolland.csv"
        self.connections_data_file = "data/ConnectiesHolland.csv"
        self.duration = 0
        self.max_num_trajects = 0
        self.total_connections = 0
        self.repeats = 0
        self.start_stations = 0


    def ask_input(self):
        print("Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL \nContributors: Daphne Westerdijk, Lieke Kollen and Willem Henkelman\n")
        print("Welcome to our case RailNL, where we try to increase the efficiency and the quality of the rail network of the Netherlands. \nPlease press the button of the map that should be used:")
        # assert self.map_size == 1 or self.map_size == 2
        self.map_size = input("1 : Holland\n2 : Netherlands\n")
        print("\nPlease select which algorithm you would like to use:")
        self.user_input = input("1 : Random\n2 : Random + Hill climber\n3 : Random greedy\n4 : Random greedy + Hill climber\n5 : Depth first\n6 : Depth first + Hill climber\n7 : Breadth first\n")
        
        self.repeats = int(input("How many times would you like to run the algorithm? We recommend running atleast x times for an accurate score."))
    
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