import copy
import random
from ..classes.traject import Traject

class Random():
    def __init__(self, map, duration, max_num_trajects):
        self.map = map
        self.duration = duration
        self.max_num_trajects = max_num_trajects + 1
        self.full_traject = {}
        self.num_allconnections = 56

    # def add_traject(self, traject_id):
    #     start_station = random.choice(list(self.map.stations))
    #     new_traject = Traject(traject_id, self.map.stations[f'{start_station}'])

    #     return new_traject

    def remove_unused_connection(self, current_station, next_station):
        for item in self.map.stations[f'{current_station}'].unused_connections:
            if item[0] == next_station[0]:
                self.map.stations[f'{current_station}'].unused_connections.remove(item)
        for item in self.map.stations[f'{next_station[0]}'].unused_connections:
            if item[0] == current_station:
                self.map.stations[f'{next_station[0]}'].unused_connections.remove(item)

        list_with_unused = []
        for station in self.map.stations:
            if self.map.stations[station].unused_connections:
                list_with_unused.append(station)
        
        self.num_allconnections = len(list_with_unused)
        print(self.num_allconnections)
    
    def doelfunctie(self, P, T, Min):
       K = P * 10000 - (T * 100 + Min)
       print(f"{K}")
       return K

    def run(self):
        # zolang niet alle verbindingen gereden zijn
        traject_id = 1
        complete_duration = 0
        while traject_id < self.max_num_trajects and self.num_allconnections > 0:
            # zolang niet het max aantal trajecten gereden is
            # while self.num_allconnections > 0:
            print(f"traject = {traject_id}")
            # initialize new traject
            # self.add_traject(traject_id)

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
                if self.map.stations[f'{current_station}'].unused_connections:
                    next_station = random.choice(self.map.stations[f'{current_station}'].unused_connections)
                # als unused connecties leeg is, gebruik een connectie uit de complete connectie lijst, is dus al gebruikt
                else:
                    next_station = random.choice(self.map.stations[f'{current_station}'].connections)
                #print(f"total duration = {new_traject.total_duration}")
                # als nieuwe connectie langer is dan max duration, maak full traject en stop traject
                if new_traject.total_duration + next_station[1] > self.duration:
                    print(f"total = {new_traject.total_duration}")
                    complete_duration += new_traject.total_duration
                    for station in new_traject.trajects:
                        self.full_traject[new_traject.traject_id].append(station)
                    traject_id += 1
                    break
                # anders, voeg de connectie toe aan het traject
                #print(current_station, next_station)
                self.remove_unused_connection(current_station, next_station)
                new_traject.add_connection(next_station)
                if self.num_allconnections == 0:
                    for station in new_traject.trajects:
                        self.full_traject[new_traject.traject_id].append(station)
                    break



                # break

        # extra print om te checken
        P = 0
        for station in self.map.stations:
            print(f"{station} met {self.map.stations[station].unused_connections}")
            P += len(self.map.stations[station].unused_connections)
        P = (56 - P)/56
        T = traject_id
        Min = complete_duration
        self.doelfunctie(P, T, Min)