import copy
import random
from ..classes.traject import Traject
from .random import Random

class Greedy(Random):

    def max_value(self, inputlist):
        value = max([sublist[-1] for sublist in inputlist])
        for items in inputlist:
            if value == items[1]:
                return items

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
                    if self.map.stations[f'{current_station}'].unused_connections:
                        next_station = self.max_value(self.map.stations[f'{current_station}'].unused_connections)
                    # als unused connecties leeg is, gebruik een connectie uit de complete connectie lijst, is dus al gebruikt
                    else:
                        next_station = self.max_value(self.map.stations[f'{current_station}'].connections)
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
