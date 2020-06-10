import random

class Random():
    def __init__(self, map, traject_list):
        self.map = map
        self.traject_list = traject_list
        self.full_traject = {}

    def run(self):
        for traject in self.traject_list:
            while traject.total_distance < 120:
                current = traject.current_station
                self.full_traject[traject.traject_id] = []
                self.full_traject[traject.traject_id].append(current)
                random_connection = random.choice(self.map.stations[f'{current}'].connections)
                if random_connection[0] not in traject.trajects:
                    traject.add_connection(random_connection)
                else:
                    for station in traject.trajects:
                        self.full_traject[traject.traject_id].append(station)
                    # print(self.full_traject)
                    break




