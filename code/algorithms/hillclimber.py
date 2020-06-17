import copy
import random
from .random import Random

class HillClimber:
    """
    class that finds train routes taking into account the heuristics using a hillclimber algorithm
    """
    def __init__(self, solution, map):
        # initialize class
        self.solution = copy.deepcopy(solution)
        self.highscore = solution.highscore
        self.hillclimber_solution = {}
        self.map = map

    def get_connections_secondtolast(self, new_result, random_traject):
        """
        method that returns the connections from the second to last station in the traject
        """
        return self.map.stations[new_result.best_traject[random_traject][-2]].connections

    def remove_time(self, new_result, random_traject):
        """
        method that removes the time of the connection which will be replaced
        """
        last_connection = new_result.best_traject[random_traject][-1]
        second_last_connection = new_result.best_traject[random_traject][-2]
        for station in self.map.stations[second_last_connection].connections:
            if station[0] == last_connection:
                new_result.complete_duration -= station[1]

    def add_connection(self, new_result, new_connection, random_traject):
        """
        method that adds the connection at the end of the traject
        """
        new_result.best_traject[random_traject][-1] = new_connection[0]
        new_result.complete_duration += new_connection[1]

    def mutate_last_connection(self, new_result):
        """
        method that mutates the last connection in a random traject
        """
        # chooses a random traject
        random_traject = random.choice(list(new_result.best_traject))
        random_traject = int(random_traject)

        # changes the last connection
        self.remove_time(new_result, random_traject)
        new_connection = random.choice(self.get_connections_secondtolast(new_result, random_traject))
        self.add_connection(new_result, new_connection, random_traject)
    
    
    def check_small_traject(self, new_result):
        """
        method that deletes trajects of only 1 connection
        """
        for traject in new_result.best_traject:
            if len(new_result.best_traject[traject]) == 2:
                del new_result.best_traject[traject]
                break

    def objectivefunction(self, P, T, Min):
        """
        method to determine the quality (K) of the set of train routes
        """
        P = (89 - P) / 89
        K = P * 10000 - (T * 100 + Min)
        return K

        
    def check_solution(self, new_result):
        """
        method that checks if the new score is better than the previous score
        """
        # Loop that goes over the trajects
        for traject in new_result.best_traject:
            # loop that goes over the stations in the traject (-1 because we want to look at the next station and the last station does not have a next station)
            for i in range(len(new_result.best_traject[traject])- 1) :
                # initialize station and next station
                station = new_result.best_traject[traject][i]
                next_station = new_result.best_traject[traject][i + 1]
                # loop that goes over the unused connections of the station
                for item in self.map.stations[station].unused_connections:
                    # if there is a connection with the next_station
                    if next_station == item[0]:
                        # remove the connection
                        self.map.stations[station].unused_connections.remove(item)
                        # remove the reversed connection
                        for reversed_connection in self.map.stations[item[0]].unused_connections:
                            if reversed_connection[0] == station:
                                self.map.stations[item[0]].unused_connections.remove(reversed_connection)

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
        P = count / 2
        T = len(new_result.best_traject)
        Min = new_result.complete_duration
        new_score = self.objectivefunction(P, T, Min)

        # checks if the new score is higher than the highscore, if so then changes the highscore
        if new_score > self.highscore:
            self.highscore = new_score
            self.hillclimber_solution = new_result.best_traject

    def run(self, iterations):
        """
        method that runs the hillclimber algorithm {iterations} amount of times
        """
        self.iterations = iterations
        print(f'Start score: {self.highscore}')

        # runs the algorithm and tracks the score
        for iteration in range(iterations):
            print(f'Iteration {iteration}/{iterations}, current score: {self.highscore}')
            new_result = copy.deepcopy(self.solution)
            self.mutate_last_connection(new_result)
            self.check_small_traject(new_result)
            self.check_solution(new_result)
