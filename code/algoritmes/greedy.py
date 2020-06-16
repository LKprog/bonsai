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
        """
        methode die het random algoritme runt voor een hoeveelheid keer dat aangegeven wordt door "num_repeats"
        """
        # begin van de while loop waarin het algoritme een x aantal keer gerund wordt
        i = 0
        while i < num_repeats:
            print(f"{i} / {num_repeats}")
            # initieer een nieuwe oplossing/resetten van de lijsten
            self.map = copy.deepcopy(self.temp)
            self.full_traject = {}
            traject_id = 1
            complete_duration = 0
            self.num_allconnections = 100
            
            # maak trajecten zolang het maximum aantal trajecten nog behaald is en nog niet alle verbindingen bereden zijn
            while traject_id < self.max_num_trajects and self.num_allconnections > 0:
                
                # maak een lijst voor stations dat nog steeds connecties hebben 
                stations_with_unused = []
                for station in self.map.stations:
                    if self.map.stations[station].unused_connections:
                        stations_with_unused.append(station)

                # creer nieuw traject met random gekozen startstation
                start_station = random.choice(stations_with_unused)
                new_traject = Traject(traject_id, self.map.stations[f'{start_station}'])
                # maak een traject lijst aan voor het huidige traject
                self.full_traject[new_traject.traject_id]= []
                
                # loop om verbindingen aan het traject toe te voegen zolang het traject nog niet 120 minuten lang duurt
                while True:
                    # stel het huidige station in
                    current_station = new_traject.current_station
                    # als er ongebruikte connecties zijn voor het huidige station, selecteer een random connectie daaruit
                    if self.map.stations[f'{current_station}'].unused_connections:
                        next_station = self.max_value(self.map.stations[f'{current_station}'].unused_connections)
                    # als unused connecties leeg is, gebruik een connectie uit de complete connectie lijst, is dus al gebruikt
                    else:
                        next_station = self.max_value(self.map.stations[f'{current_station}'].connections)
                    # als nieuwe connectie langer de duratie langer maakt dan de maximale duratie, maak het complete traject aan stop het traject
                    if new_traject.total_duration + next_station[1] > self.duration or self.num_allconnections == 0:
                        complete_duration += new_traject.total_duration
                        for station in new_traject.trajects:
                            self.full_traject[new_traject.traject_id].append(station)
                        traject_id += 1
                        break
                    # anders, verwijder de connectie uit de ongebruikte connectie lijst en voeg de connectie toe aan het traject
                    self.remove_unused_connection(current_station, next_station)
                    new_traject.add_connection(next_station)
                   
            # bereken de score van de complete run
            score = self.doelfunctie(self.num_allconnections, traject_id, complete_duration)
            
            # als de score boven de lowerbound zit en daarmee dus alle connecties heeft bereden ga naar de volgende run, anders overschrijf de run
            if score > self.lower_bound:
                self.score_list.append(int(score))
                self.best_score(score, self.full_traject, complete_duration)
                i += 1