import copy
import random
from ..classes.traject import Traject


class Random():
    def __init__(self, map, duration, max_num_trajects):
        self.map = map
        self.duration = duration
        self.max_num_trajects = max_num_trajects
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
        self.num_allconnections -= 2
        print(self.num_allconnections)
        # print(current_station)
        # for station in self.map.stations:
        #     print(f"{station} met {self.map.stations[station].unused_connections}")

    def run(self):
        # zolang niet alle verbindingen gereden zijn
        traject_id = 1
        while traject_id <  8:
            # zolang niet het max aantal trajecten gereden is
            while self.num_allconnections > 0:
                print(f"traject = {traject_id}")
                # initialize new traject
                # self.add_traject(traject_id)
                start_station = random.choice(list(self.map.stations))
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
                    print(f"total duration = {new_traject.total_duration}")
                    # als nieuwe connectie langer is dan max duration, maak full traject en stop traject
                    if new_traject.total_duration + next_station[1] > 120:
                        print(f"total = {new_traject.total_duration}")
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        traject_id += 1
                        break
                    # anders, voeg de connectie toe aan het traject
                    print(current_station, next_station)
                    self.remove_unused_connection(current_station, next_station)
                    new_traject.add_connection(next_station)
                    if self.num_allconnections == 0:
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        break
            break

        # extra print om te checken
        for station in self.map.stations:
            print(f"{station} met {self.map.stations[station].unused_connections}")







            # all_stations = []
            # for number in self.full_traject:
            #     for station in self.full_traject[number]:
            #         if station not in all_stations:
            #             all_stations.append(station)
                        
            # self.num_allstations = len(all_stations)
            # print(self.num_allstations)





    # traject_list = []
    # i = 0
    # while i < 7:
    #     start_station = random.choice(list(test.stations))
    #     new_traject = Traject(i, test.stations[f'{start_station}'])
    #     traject_list.append(new_traject)
    #     i += 1

    # def run(self):
    #     # zolang niet alle verbindingen gereden zijn
    #     while self.num_allstations != 28: 
    #         # per traject van de 7, selecteer het start station random
    #         for traject in self.traject_list:
    #             traject.current_station = random.choice(list(self.map.stations))
    #             # start station, en append die aan het traject
    #             current = traject.current_station
    #             self.full_traject[traject.traject_id] = []
    #             self.full_traject[traject.traject_id].append(current)
    #             print(traject.traject_id)
    #             print(current)
    #             # zolang de maximale duratie niet bereikt word
    #             while traject.total_distance < 120:
    #                 # huidig station
    #                 current = traject.current_station
    #                 # selecteer een random connectie die dat station heeft
    #                 random_connection = random.choice(self.map.stations[f'{current}'].connections)
    #                 # als die connectie nog niet in het traject zit
    #                 if random_connection[0] not in traject.trajects:
    #                     traject.add_connection(random_connection)
    #                     print(self.map.stations[f'{current}'].connections)
    #                     print(traject.total_distance)
    #                     self.map.stations[f'{current}'].connections.remove(random_connection)
    #                     print(self.map.stations[f'{current}'].connections)

    #                 if self.map.stations[f'{current}'].connections is []:
    #                     for connection in self.map.all_connections:
    #                         self.map.stations[f'{current}'].connections.append(connection)

    #             print("hoi")
    #             for station in traject.trajects:
    #                 self.full_traject[traject.traject_id].append(station)
                        
    #             all_stations = []
    #             for number in self.full_traject:
    #                 for station in self.full_traject[number]:
    #                     if station not in all_stations:
    #                         all_stations.append(station)
                        
    #         self.num_allstations = len(all_stations)
    #         print(self.num_allstations)




