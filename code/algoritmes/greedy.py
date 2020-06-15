import copy
import random
from ..classes.traject import Traject

class Greedy():
    def __init__(self, map, duration, max_num_trajects):
        self.map = map
        self.duration = duration
        self.max_num_trajects = max_num_trajects + 1
        self.full_traject = {}
        self.num_allconnections = 56
        self.temp = copy.deepcopy(map)
        self.highscore = 0
        self.best_traject = {}
        self.complete_duration = 0

    # def add_traject(self, traject_id):
    #     start_station = random.choice(list(self.map.stations))
    #     new_traject = Traject(traject_id, self.map.stations[f'{start_station}'])

    #     return new_traject

    def remove_unused_connection(self, current_station, next_station):
        for item in self.map.stations[f'{current_station}'].unused_connections:
            if item[0] == next_station[0]:
                self.map.stations[f'{current_station}'].unused_connections.remove(item)
        for item in self.map.stations[f'{next_station[0]}'].unused_connections:
            if item[0] == str(current_station):
                self.map.stations[f'{next_station[0]}'].unused_connections.remove(item)

        list_with_unused = []
        for station in self.map.stations:
            if self.map.stations[station].unused_connections:
                list_with_unused.append(station)
        
        self.num_allconnections = len(list_with_unused)
    
    def doelfunctie(self, P, T, Min):
       K = P * 10000 - (T * 100 + Min)
       return K
    
    def best_score(self, score, full_traject, complete_duration):
        if self.highscore == 0 or score > self.highscore:
            self.highscore = score
            self.best_traject = full_traject
            self.complete_duration = complete_duration
    
    def run(self, num_repeats):
        i = 0
        while i < num_repeats:
            print(f"{i} / {num_repeats}")
            self.map = copy.deepcopy(self.temp)
            self.full_traject = {}
            # zolang niet alle verbindingen gereden zijn
            traject_id = 1
            complete_duration = 0
            self.num_allconnections = 56
            while traject_id < self.max_num_trajects and self.num_allconnections > 0:

                stations_with_unused = []
                for station in self.map.stations:
                    if self.map.stations[station].unused_connections:
                        stations_with_unused.append(station)

                start_station = random.choice(stations_with_unused)
                new_traject = Traject(traject_id, self.map.stations[f'{start_station}'])
                self.full_traject[new_traject.traject_id]= []
                # zolang de max tijd nog niet gebruikt is
                while True:
                    # stel current station in
                    current_station = new_traject.current_station
                    # selecteer random connection/station uit de unused connecties

# aanpassen
                    if self.map.stations[f'{current_station}'].unused_connections:
                        next_station = random.choice(self.map.stations[f'{current_station}'].unused_connections)
                    # als unused connecties leeg is, gebruik een connectie uit de complete connectie lijst, is dus al gebruikt
                    else:
                        next_station = random.choice(self.map.stations[f'{current_station}'].connections)
                    # als nieuwe connectie langer is dan max duration, maak full traject en stop traject
                    if new_traject.total_duration + next_station[1] > self.duration:
                        complete_duration += new_traject.total_duration
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        traject_id += 1
                        break
                    # anders, voeg de connectie toe aan het traject
                    self.remove_unused_connection(current_station, next_station)
                    new_traject.add_connection(next_station)
                    if self.num_allconnections == 0:
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        complete_duration += new_traject.total_duration
                        break
                    # break

            P = 0
            for station in self.map.stations:
                P += len(self.map.stations[station].unused_connections)
            P = (56 - P) / 56
            T = traject_id
            Min = complete_duration
            score = self.doelfunctie(P, T, Min)
            self.best_score(score, self.full_traject, Min)
            i += 1

# nodig: connectielijst met duration in init

# 1: kies station met minste connecties
# 2: kies de connectie met de langste duration
# 3: move naar dat station
# 4: haal connectie van de lijst, haal duration van de 120 af
# 5; repeat 2-4 tot 0 minuten
# 6: ga vanaf stap 1
