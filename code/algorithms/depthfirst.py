"""
 * depthfirst.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""
import copy


class Depthfirst:
    """
    class that finds train routes taking into account the heuristics using a depth first algorithm.
    """
    
    def __init__(self, map):
        # initialize class
        self.map = copy.deepcopy(map)
        self.stations_list = [copy.deepcopy(self.map.stations)]
        self.best_value = 0
        self.best_time = float('inf')
        self.solution_list = []
        self.best_solution = []
        self.ultimate_solution = {}

    def get_next_state(self, stack):
        """
        method that gets the next item from the stack.
        """
        return stack.pop()


    def check_solution(self):
        """
        method that checks the solution and returns the traject with the most connections used and lowest duration.
        """
        
        # for every start station
        for start in list(self.ultimate_solution):

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
            self.best_time = 180

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
            
            # Add the solutions to the ultimate solution dictionary
            self.ultimate_solution[start] = self.best_solution

    def run(self, duration, start_stations):
        """
        method that runs the depth first algorithm.
        """
        
        # initialize the variables
        stack = start_stations
        start = copy.deepcopy(start_stations)

        # while there are still items in the stack
        while len(stack)> 0:
            # get the next start station from the list
            state= self.get_next_state(stack)
            
            # if state is a start station
            if state in start:
                print(f"New start station: {state}")
                # make a key in the ultimate_solution
                self.ultimate_solution[state] = []
                
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
                        if child[0] + connection[1] <= 120:
                            child.append(connection[0])
                            child[0] += connection[1]
                            stack.append(child)
                        
                        # else:
                        # only unique children are added to the solution list
                        elif child not in self.solution_list:
                                self.solution_list.append(child)
        
        # check the solution         
        self.check_solution()
