import copy


class Depthfirst:
    def __init__(self, map):
        self.map = copy.deepcopy(map)
        self.stations_list = [copy.deepcopy(self.map.stations)]
        self.best_value = 0
        self.best_time = float('inf')
        self.best_solution = []
        self.solution_list = []
        self.ultimate_solution = {}

    def check_solution(self):
        for start in list(self.ultimate_solution):
            for traject in self.solution_list:
                if traject[1] == start:
                    score = len(traject) - 1
                    if score == self.best_value:
                        self.best_solution.append(traject)
                    if score > self.best_value:
                        self.best_solution = []
                        self.best_value = score
                        self.best_solution.append(traject)

            self.best_time = 200
            for solution in self.best_solution:
                if solution[1] == start:
                    if solution[0] == self.best_time:
                        self.best_solution.append(solution)
                    if solution[0] < self.best_time:
                        self.best_time = solution[0]
                        self.best_solution = []
                        self.best_solution.append(solution)
            self.ultimate_solution[start] = self.best_solution

    def run(self, duration, start_stations):
        stack = start_stations
        start = copy.deepcopy(start_stations)
        depth = 200
        count = 0
        while len(stack)> 0:
            state=stack.pop()
            if len(state) < depth:
                if state in start:
                    self.ultimate_solution[state] = []
                    for i in self.map.stations[state].connections:
                        child = [0, copy.deepcopy(state)]
                        child.append(i[0])
                        child[0] += i[1]
                        stack.append(child)
                        count += 1
                else:
                    for i in self.map.stations[state[-1]].connections:
                        if i[0] not in state:
                            child = copy.deepcopy(state)
                            if child[0] + i[1] <= 120:
                                child.append(i[0])
                                child[0] += i[1]
                                stack.append(child)
                                count += 1
                            else:
                                if child not in self.solution_list:
                                    self.solution_list.append(child)         
        self.check_solution()
