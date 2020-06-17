import copy
import random
from .random import Random

class HillClimber:
    def __init__(self, solution, map):
        self.solution = copy.deepcopy(solution)
        self.highscore = solution.highscore
        self.map = map

    def get_connections_secondtolast(self, new_result, random_traject):
        return self.map.stations[new_result.best_traject[random_traject][-2]].connections

    def remove_time(self, new_result, random_traject):
        last_connection = new_result.best_traject[random_traject][-1]
        second_last_connection = new_result.best_traject[random_traject][-2]
        for station in self.map.stations[second_last_connection].connections:
            if station[0] == last_connection:
                print(new_result.complete_duration)
                new_result.complete_duration -= station[1]

    def add_connection(self, new_result, new_connection, random_traject):
        new_result.best_traject[random_traject][-1] = new_connection[0]
        new_result.complete_duration += new_connection[1]

    def mutate_last_connection(self, new_result):
        random_traject = random.choice(list(new_result.best_traject))
        random_traject = int(random_traject)
        print(new_result.best_traject[random_traject])
        print(self.get_connections_secondtolast(new_result, random_traject)) 
        self.remove_time(new_result, random_traject)
        new_connection = random.choice(self.get_connections_secondtolast(new_result, random_traject))
        print(new_connection[0])
        self.add_connection(new_result, new_connection, random_traject)
        print(new_result.best_traject[random_traject])
        print(new_result.complete_duration)

        
    def check_solution(self, new_result):
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
        print(list_with_unused)

        count = 0
        for station in list_with_unused:
            for connection in self.map.stations[station].unused_connections:
                count += 1

        print(89 - count)
# Naar een P omzetten voor de doelfunctie

    def run(self, iterations):
        new_result = copy.deepcopy(self.solution)
        self.mutate_last_connection(new_result)

        self.check_solution(new_result)

