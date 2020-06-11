import random

class Random():
    def __init__(self, map, traject_list):
        self.map = map
        self.traject_list = traject_list
        self.full_traject = {}
        self.num_allstations = 0

    def run(self):
        while self.num_allstations != 28: 
            for traject in self.traject_list:
                traject.current_station = random.choice(list(self.map.stations))
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
                        
                        all_stations = []
                        for number in self.full_traject:
                            for station in self.full_traject[number]:
                                if station not in all_stations:
                                    all_stations.append(station)
                        break
            self.num_allstations = len(all_stations)
            print(self.num_allstations)




