"""
 * random.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Random algorithm with the following heuristics:
 *      - maximum of 7 train routes (Dutch: traject)
 *      - every train route can have a maximum duration of 120 minutes
 *      - a connection between stations can be used both ways
 *      - every new train route starts with a randomly chosen station from a list of that tracks stations that still have unused connections 
 *      - for every train route, connections will first be randomly chosen from a list that tracks the unused connections of the current station
"""

import copy
import random
from ..classes.traject import Traject

class Random():
    """
    class that finds train routes taking into account the heuristics using a random algorithm
    """
    def __init__(self, map, duration, max_num_trajects, lower_bound):
        # initialize class
        self.map = map
        self.duration = duration
        self.max_num_trajects = max_num_trajects + 1
        self.lower_bound = lower_bound
        self.full_traject = {}
        self.num_allconnections = 56
        self.temp = copy.deepcopy(map)
        self.highscore = 0
        self.best_traject = {}
        self.complete_duration = 0
        self.score_list = []
    

    def remove_unused_connection(self, current_station, next_station):
        """
        method that updates the list of unused connections by removing used connections from the list of the relevant station
        """
        # loop to remove used connection from stations in both directions
        for item in self.map.stations[f'{current_station}'].unused_connections:
            if item[0] == next_station[0]:
                self.map.stations[f'{current_station}'].unused_connections.remove(item)
        for item in self.map.stations[f'{next_station[0]}'].unused_connections:
            if item[0] == str(current_station):
                self.map.stations[f'{next_station[0]}'].unused_connections.remove(item)
        
        # list of stations that have unused connections
        list_with_unused = []
        for station in self.map.stations:
            if self.map.stations[station].unused_connections:
                list_with_unused.append(station)
        
        #  contains the number of stations with unused connections
        self.num_allconnections = len(list_with_unused)
    
    
    def objectivefunction(self, P, T, Min):
        """
        method to determine the quality (K) of the set of train routes
        """
        P = (56 - P) / 56
        T = T - 1
        K = P * 10000 - (T * 100 + Min)
        return K
    
    
    def best_score(self, score, full_traject, complete_duration):
        """
        method that saves the highest quality score and it's corresponding train routes and the duration
        """
        if self.highscore == 0 or score > self.highscore:
            self.highscore = score
            self.best_traject = full_traject
            self.complete_duration = complete_duration
    
    
    def run(self, num_repeats):
        """
        method that runs the random algorithm an "num_repeats" amount of times
        """
        # while loop that makes sure the algorithm is run x amount of times
        i = 0
        while i < num_repeats:
            if i%1000 == 0:
                print(f"{i} / {num_repeats}")
            # initialize a new set of solution/reset the lists
            self.map = copy.deepcopy(self.temp)
            self.full_traject = {}
            traject_id = 1
            complete_duration = 0
            self.num_allconnections = 100
            
            # make new train routes as long as the maximum number of routes is not reached and all connections are not used
            while traject_id < self.max_num_trajects and self.num_allconnections > 0:
                
                # list of stations that still have unused connections
                stations_with_unused = []
                for station in self.map.stations:
                    if self.map.stations[station].unused_connections:
                        stations_with_unused.append(station)

                # create a new train route with a randomly chosen station from the list of stations that have unused connections
                start_station = random.choice(stations_with_unused)
                new_traject = Traject(traject_id, self.map.stations[f'{start_station}'])
                # make a list of the connections for the current train route
                self.full_traject[new_traject.traject_id]= []
                
                # loop to add connections to the train route until the maximum duration is not reached
                while True:
                    # set current station
                    current_station = new_traject.current_station
                    # if the current station has unused connections, randomly select one of them
                    if self.map.stations[f'{current_station}'].unused_connections:
                        # print(self.duration - new_traject.total_duration)
                        unused_connection_within_duration = []
                        for connection in self.map.stations[f'{current_station}'].unused_connections:
                            if connection[1] <= self.duration - new_traject.total_duration:
                                unused_connection_within_duration.append(connection)
                        if unused_connection_within_duration:
                            next_station = random.choice(unused_connection_within_duration)
                        # print(next_station)
                        else:
                            # next_station = random.choice(self.map.stations[f'{current_station}'].connections)
                            complete_duration += new_traject.total_duration
                            for station in new_traject.trajects:
                                self.full_traject[new_traject.traject_id].append(station)
                            traject_id += 1
                            break
                
                    # if the current stations does not have unused connections, randomly select a connection that has been used
                    else:
                        next_station = random.choice(self.map.stations[f'{current_station}'].connections)

                    # if the new connections makes the duration longer than the maximum duration or all if all connections have been used, stop the train route
                    if new_traject.total_duration + next_station[1] > self.duration or self.num_allconnections == 0:
                        complete_duration += new_traject.total_duration
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        traject_id += 1
                        break
                    # else, add the connection to the route and remove from the unused connections list
                    self.remove_unused_connection(current_station, next_station)
                    new_traject.add_connection(next_station)
                   
            # calculate the score of the objective function for the complete set of train routes
            score = self.objectivefunction(self.num_allconnections, traject_id, complete_duration)
            self.score_list.append(score)
            self.best_score(score, self.full_traject, complete_duration)
            i += 1
            
            # # als de score boven de lowerbound zit en daarmee dus alle connecties heeft bereden ga naar de volgende run, anders overschrijf de run
            # if score > self.lower_bound:
            #     self.score_list.append(score)
            #     self.best_score(score, self.full_traject, complete_duration)
            #     i += 1