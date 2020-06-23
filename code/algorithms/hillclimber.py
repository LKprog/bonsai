"""
 * hillclimber.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Iterative algorithm that searches for a better solution by making changes to an already exisiting solution
"""

import copy
import random
from .randomize import Random

class HillClimber:
    """
    class that finds train routes taking into account the heuristics using a hillclimber algorithm
    """

    def __init__(self, solution, map, total_connections):
        """
        initialize the class and all it's corresponding variables
        """

        self.solution = copy.deepcopy(solution)
        self.highscore = solution.highscore
        self.hillclimber_solution = solution.best_traject
        self.map = copy.deepcopy(map)
        self.copy = copy.deepcopy(map)
        self.total_connections = total_connections

    def get_connections_secondtolast(self, new_result, random_traject):
        """
        method that returns the connections from the second to last station in the traject
        """

        return self.map.stations[new_result.best_traject[random_traject][-2]].connections

    def get_connections_second(self, new_result, random_traject):
        """
        method that returns the connections from the second to last station in the traject
        """

        return self.map.stations[new_result.best_traject[random_traject][1]].connections

    def remove_last(self, new_result, random_traject):
        """
        method that removes the time of the last connection (which will be replaced)
        """

        last_connection = new_result.best_traject[random_traject][-1]
        second_last_connection = new_result.best_traject[random_traject][-2]
        for station in self.map.stations[second_last_connection].connections:
            if station[0] == last_connection:
                new_result.complete_duration -= station[1]

    def remove_first(self, new_result, random_traject):
        """
        method that removes the time of the start connection (which will be replaced)
        """

        first_connection = new_result.best_traject[random_traject][0]
        second_connection = new_result.best_traject[random_traject][1]
        for station in self.map.stations[second_connection].connections:
            if station[0] == first_connection:
                new_result.complete_duration -= station[1]

    def add_connection_last(self, new_result, new_connection, random_traject):
        """
        method that adds the connection at the end of the traject
        """

        new_result.best_traject[random_traject][-1] = new_connection[0]
        new_result.complete_duration += new_connection[1]

    def add_connection_first(self, new_result, new_connection, random_traject):
        """
        method that adds the connection at the start of the traject
        """

        new_result.best_traject[random_traject][0] = new_connection[0]
        new_result.complete_duration += new_connection[1]

    def mutate_last_connection(self, new_result):
        """
        method that mutates the last connection in a random traject
        """

        # chooses a random traject
        random_traject = random.choice(list(new_result.best_traject))
        random_traject = int(random_traject)

        # changes the last connection
        self.remove_last(new_result, random_traject)
        new_connection = random.choice(self.get_connections_secondtolast(new_result, random_traject))
        self.add_connection_last(new_result, new_connection, random_traject)

    def mutate_first_connection(self, new_result):
        """
        method that mutates the first connection in a random traject
        """

        # chooses a random traject
        random_traject = random.choice(list(new_result.best_traject))
        random_traject = int(random_traject)

        # changes the first connection
        self.remove_first(new_result, random_traject)
        new_connection = random.choice(self.get_connections_second(new_result, random_traject))
        self.add_connection_first(new_result, new_connection, random_traject)

    def objectivefunction(self, P, T, Min):
        """
        method to determine the quality (K) of the set of train routes, where P is the fraction of used connections, T is number of routes used and Min is the total duration of all routes
        """

        P = (self.total_connections - (P/2)) / self.total_connections
        T = len(T)
        K = P * 10000 - (T * 100 + Min)
        return K


    def check_solution(self, new_result):
        """
        method that checks if the new score is better than the previous score
        """

        # loop that goes over the trajects
        for traject in new_result.best_traject:

            # loop that goes over the stations in the traject (-1 because we want to look at the next station and the last station does not have a next station)
            for i in range(len(new_result.best_traject[traject])- 1):

                # initialize station and next station
                station = new_result.best_traject[traject][i]
                next_station = new_result.best_traject[traject][i + 1]

                # loop that goes over the unused connections of the station
                for connection in self.map.stations[station].unused_connections:

                    # if there is a connection with the next_station
                    if next_station == connection[0]:

                        # remove the connection from unused connection list
                        self.map.stations[station].unused_connections.remove(connection)

                        # remove the reversed connection from unused connection list
                        for reversed_connection in self.map.stations[connection[0]].unused_connections:

                            if reversed_connection[0] == station:
                                self.map.stations[connection[0]].unused_connections.remove(reversed_connection)

        # check if there are stations left with unused connections (if empty -> P=1)
        list_with_unused = []

        for station in self.map.stations:

            if self.map.stations[station].unused_connections:
                list_with_unused.append(station)

        # counts how many connections are still unused
        count = 0

        for station in list_with_unused:

            for connection in self.map.stations[station].unused_connections:
                count += 1

        # calculates the score of the traject
        new_score = self.objectivefunction(count, list(new_result.best_traject), new_result.complete_duration)

        # checks if the new score is higher than the highscore, if so then changes the highscore
        if new_score > self.highscore:
            self.highscore = new_score
            self.hillclimber_solution = new_result.best_traject

    def run(self, iterations):
        """
        method that runs the hillclimber algorithm {iterations} amount of times
        """

        # print(f'Start score: {self.highscore}')

        # runs the algorithm and tracks the score
        for iteration in range(iterations):
            self.map = copy.deepcopy(self.copy)
            new_result = copy.deepcopy(self.solution)
            self.mutate_last_connection(new_result)
            self.mutate_first_connection(new_result)
            self.check_solution(new_result)
