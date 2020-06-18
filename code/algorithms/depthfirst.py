import copy


class Depthfirst:
    def __init__(self, map):
        self.map = copy.deepcopy(map)
        self.stations_list = [copy.deepcopy(self.map.stations)]
        self.best_value = 0
        self.best_solution = []

    # def get_next_station(self):
    #     return self.map.stations.pop()

    # def build_children(self, current_station, map):
    #     values = self.map.stations[current_station].connections
    #
    #     for value in values:
    #         create new traject

    def check_solution(self, stack):
        for traject in stack:
            score = len(traject)
            if score > self.best_value:
                self.best_value = score
                self.best_solution = traject

                print(self.best_value)

    def run(self, duration, start_station):
        stack = [start_station]
        count = 0

        while len(stack)>0:
            print(stack)
            state=stack.pop()
                # print(count)
            total_duration = 0
            # print(state)
            if total_duration < duration:
                if count == 0:
                    for i in self.map.stations[state].connections:
                    
                        child = [copy.deepcopy(state)]
                        # print(child)
                        child.append(i[0])
                        total_duration += i[1]
                        stack.append(child)
                        count += 1
                else:
                    for i in self.map.stations[state[-1]].connections:
                        child = [copy.deepcopy(state)]
                        # print(child)
                        child.append(i[0])
                        total_duration += i[1]
                        stack.append(child)
                        count += 1
            self.check_solution(stack)
