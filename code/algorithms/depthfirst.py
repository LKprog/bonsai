"""
 * depthfirst.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""
import copy
import random


class Depthfirst:
    """
    class that finds train routes taking into account the heuristics using a depth first algorithm.
    """

    def __init__(self, map, total_connections, amount_trajects):
        # initialize class
        self.map = copy.deepcopy(map)
        self.stations_list = [copy.deepcopy(self.map.stations)]
        self.best_value = 0
        self.best_time = float('inf')
        self.solution_list = []
        self.best_solution = []
        self.final_solution = {}
        self.total_connections = total_connections
        self.score_list = []

        self.amount_trajects = amount_trajects
        self.best_score = 0
        self.best_result = None

    def get_next_state(self, stack):
        """
        method that gets the next item from the stack.
        """

        return stack.pop()

    def get_start_stations(self):
        """
        method that sets a random station to start the new traject from.
        """

        start_stations = []
        count = 0
        while count < self.amount_trajects:
            start = random.choice(list(self.map.stations))
            if start not in start_stations:
                start_stations.append(start)
                count += 1
        return start_stations


    def check_solution(self):
        """
        method that checks the solution and returns the traject with the most connections used and lowest duration.
        """

        # for every start station
        for start in list(self.final_solution):

            # loop over the trajects
            for traject in self.solution_list:

                # pick the trajects with the same start station
                if traject[1] == start:

                    # how long is the traject
                    score = len(traject) - 1
                    self.best_value = 0

                    # if the score is as high as the best score then add to best solution list
                    if score == self.best_value:
                        self.best_solution.append(traject)

                    # if the score is higher than the best score then empty the best solution list and add the new best traject
                    elif score > self.best_value:
                        self.best_solution = []
                        self.best_value = score
                        self.best_solution.append(traject)

            # everytime a new start station is used, initialize the best time to max time (180 min)
            self.best_time = 181

            # loops over the solutions in best solution list
            for solution in self.best_solution:

                # pick the trajects with the same start station
                if solution[1] == start:

                    # if the duration is the same as the best time then add to best solution list
                    if solution[0] == self.best_time:
                        self.best_solution.append(solution)

                    # if the duration is lower than the best time, empty the best solution list and add the new best traject
                    elif solution[0] < self.best_time:

                        self.best_time = solution[0]
                        self.best_solution = []
                        self.best_solution.append(solution)

            # Add the solutions to the final_solution dictionary
            self.final_solution[start] = self.best_solution[0]

    def calculate_p(self):
        """
        method that calculates the fraction of unused connections.
        """

        list_connections_used = []
        count = 0

        # count all unique connections made in the solution
        for traject in self.final_solution:
            station = self.final_solution[traject]
            for i in range(len(station)):
                if i == 0 or i == (len(station) - 1):
                    continue
                elif [station[i], station[i + 1]] not in list_connections_used:
                    list_connections_used.append([station[i], station[i + 1]])
                    list_connections_used.append([station[i + 1], station[i]])
                    count += 2

        return count

    def calculate_min(self):
        """
        method that calculates the total duration of all routes together.
        """

        total_min = 0
        for traject in self.final_solution:
            total_min += self.final_solution[traject][0]
        return total_min

    def objectivefunction(self, P, T, Min):
        """
        method to determine the quality (K) of the set of train routes, where P is the fraction of used connections, T is number of routes used and Min is the total duration of all routes
        """

        P = P / self.total_connections
        T = len(T)
        K = P * 10000 - (T * 100 + Min)
        return K

    def run(self, num_repeats, duration):
        """
        method that runs the depth first algorithm.
        """

        for i in range(num_repeats):
            # initializing variables
            print(f"{i}/{num_repeats}")
            self.final_solution = {}
            stack = self.get_start_stations()
            start = copy.deepcopy(stack)

            # while there are still items in the stack
            while len(stack)> 0:

                # get the next start station from the list
                state= self.get_next_state(stack)

                # if state is a start station
                if state in start:
                    # make a key in the final_solution
                    self.final_solution[state] = []

                    # for every connection from the start station, make a new child
                    for connection in self.map.stations[state].connections:
                        child = [0, copy.deepcopy(state)]
                        child.append(connection[0])
                        child[0] += connection[1]
                        stack.append(child)

                # if the state is not a start station
                else:

                    # get the connections from the last station in the traject and make for every connection a new child
                    for connection in self.map.stations[state[-1]].connections:
                        if connection[0] not in state:
                            child = copy.deepcopy(state)
                            if child[0] + connection[1] <= duration:
                                child.append(connection[0])
                                child[0] += connection[1]
                                stack.append(child)

                            # else:
                            # only unique children are added to the solution list
                            elif child not in self.solution_list:
                                    self.solution_list.append(child)

            # check the solution
            self.check_solution()
            score = self.objectivefunction(self.calculate_p(), self.final_solution , self.calculate_min())
            self.score_list.append(score)

            if score > self.best_score:
                self.best_score = score
                self.best_result = self.final_solution

        # change the format of the result for later transformation to csv
        count = 1
        copy_result = copy.deepcopy(self.best_result)
        
        for traject in copy_result:
            self.best_result[traject].remove(self.best_result[traject][0])
            self.best_result[count] = self.best_result.pop(traject)
            count += 1
