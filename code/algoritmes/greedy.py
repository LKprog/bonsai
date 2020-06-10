import copy
import random

class Greedy:

        def __init__(self, map, traject_list):
                self.map = copy.deepcopy(map)
                self.traject_list = traject_list
                self.trajects = []

        def greedy_start(new_traject):
                # print(new_traject.current_station)
                print(new_traject.trajects)
                print(new_traject.total_distance)

        def run(self):
                # kiest een random startpunt
                stations_list = []
                for new_traject in self.traject_list:
                        while True:
                                current = new_traject.current_station
                                self.trajects.append(current)
                                random_connection = random.choice(self.map.stations[f'{current}'].connections)
                                if random_connection[1] + new_traject.total_distance > 120:
                                        self.trajects.append(new_traject)
                                        break
                                # als de random connectie niet al eerder is bezocht dan wordt hij aan het traject toegevoegd
                                if random_connection[0] not in new_traject.trajects:
                                        new_traject.add_connection(random_connection)
                                else:
                                        break
