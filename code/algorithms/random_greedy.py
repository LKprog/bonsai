"""
 * random_greedy.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""

import copy
import random
from ..classes.traject import Traject
from .randomize import Random

class Greedy(Random):
    """
    class that finds the most optimal train routes taking into account the heuristics using a random-greedy algorithm
    """

    def max_value(self, inputlist):
        """
        method that returns the connection with the longest duration
        """

        value = max([sublist[-1] for sublist in inputlist])
        for item in inputlist:
            if value == item[1]:
                return item

    def min_value(self, inputlist):
        """
        method that returns the connection with the shortest duration
        """

        value = min([sublist[-1] for sublist in inputlist])
        for item in inputlist:
            if value == item[1]:
                return item


    def run(self, num_repeats, min_max):
        """
        method that runs the random greedy algorithm an "num_repeats" amount of times
        """

        # while loop that makes sure the algorithm is run x amount of times
        for i in range(num_repeats):

            if i%1000 == 0 and num_repeats != 1:
                print(f"{i} / {num_repeats}")

            # initialize a new set of solution/reset the lists
            self.reset_variables()

            # make new train routes as long as the maximum number of routes is not reached and all connections are not used
            while self.traject_id < self.max_num_trajects and self.num_allconnections > 0:

                # list of stations that still have unused connections
                stations_with_unused = []

                for station in self.map.stations:

                    if self.map.stations[station].unused_connections:
                        stations_with_unused.append(station)

                # create a new train route with a randomly chosen station from the list of stations that have unused connections
                start_station = random.choice(stations_with_unused)
                new_traject = Traject(self.traject_id, self.map.stations[f'{start_station}'])

                # make a list of the connections for the current train route
                self.full_traject[new_traject.traject_id]= []

                # loop to add connections to the train route until the maximum duration is not reached
                while True:

                    # set current station
                    current_station = new_traject.current_station

                    # if the current station has unused connections, randomly select one of them
                    if self.map.stations[f'{current_station}'].unused_connections:

                        if min_max == 'max':
                            next_station = self.max_value(self.map.stations[f'{current_station}'].unused_connections)

                        elif min_max == 'min':
                            next_station = self.min_value(self.map.stations[f'{current_station}'].unused_connections)

                    # if the current stations does not have unused connections, randomly select a connection that has been used
                    else:
                        if min_max == 'max':
                            next_station = self.max_value(self.map.stations[f'{current_station}'].connections)

                        elif min_max == 'min':
                            next_station = self.min_value(self.map.stations[f'{current_station}'].connections)

                    # if the new connections makes the duration longer than the maximum duration or all if all connections have been used, stop the train route
                    if new_traject.total_duration + next_station[1] > self.duration or self.num_allconnections == 0:
                        self.end_traject(new_traject.total_duration, new_traject)
                        break

                    # else, add the connection to the route and remove from the unused connections list
                    self.remove_unused_connection(current_station, next_station)
                    new_traject.add_connection(next_station)

            # calculate the score of the objective function for the complete set of train routesun
            score = self.objectivefunction(self.num_allconnections, self.traject_id, self.traject_duration)
            self.score_list.append(int(score))
            self.best_score(score, self.full_traject, self.traject_duration)
