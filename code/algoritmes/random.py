"""
 * random.py
 *
 * Minor programmeren UvA - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Random algoritme met de volgende heuristieken:
 *      - maximum van 7 trajecten
 *      - elk traject mag maximaal 120 minuten duren
 *      - verbinding tussen stations kan beide richtingen op gaan
 *      - elk nieuw traject kiest random een station uit dat nog ongebruikte verbindingen heeft
 *      - ongebruikte verbindingen worden als eerst gekozen voor het traject, anders gebruikte verbindingen
"""

import copy
import random
from ..classes.traject import Traject

class Random():
    """
    Random algoritme class die random oplossingen vind voor de lijnvoering rekening houdend met de heuristieken
    """
    def __init__(self, map, duration, max_num_trajects):
        # initiëren van de random class
        self.map = map
        self.duration = duration
        self.max_num_trajects = max_num_trajects + 1
        self.full_traject = {}
        self.num_allconnections = 56
        self.temp = copy.deepcopy(map)
        self.highscore = 0
        self.best_traject = {}
        self.complete_duration = 0
    

    def remove_unused_connection(self, current_station, next_station):
        """
        methode die de lijst van ongebruikte connecties update door gebruikte connecties te verwijderen uit de lijst van het betreffende station
        """
        # loops om de verbindingen vanuit beide richtingen te verwijderen uit de lijst
        for item in self.map.stations[f'{current_station}'].unused_connections:
            if item[0] == next_station[0]:
                self.map.stations[f'{current_station}'].unused_connections.remove(item)
        for item in self.map.stations[f'{next_station[0]}'].unused_connections:
            if item[0] == str(current_station):
                self.map.stations[f'{next_station[0]}'].unused_connections.remove(item)
        
        # lijst van stations met ongebruikte connecties
        list_with_unused = []
        for station in self.map.stations:
            if self.map.stations[station].unused_connections:
                list_with_unused.append(station)
        
        #  houd het aantal stations met ongebruikte connecties bij
        self.num_allconnections = len(list_with_unused)
    
    
    def doelfunctie(self, P, T, Min):
        """
        methode om de kwaliteit te bepalen op basis van de gegeven doelfunctie
        """
        P = (56 - P) / 56
        T = T - 1
        K = P * 10000 - (T * 100 + Min)
        return K
    
    
    def best_score(self, score, full_traject, complete_duration):
        """
        methode die hoogste score opslaat en bijhoud met het bijbehorende traject plus tijd tijdens de method "run"
        """
        if self.highscore == 0 or score > self.highscore:
            self.highscore = score
            self.best_traject = full_traject
            self.complete_duration = complete_duration
    
    
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
            self.num_allconnections = 22
            
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
                        next_station = random.choice(self.map.stations[f'{current_station}'].unused_connections)
                    # als de unused connecties lijst leeg is, gebruik een connectie uit de gehele connectie lijst
                    else:
                        next_station = random.choice(self.map.stations[f'{current_station}'].connections)
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
            if score > 8460:
                self.best_score(score, self.full_traject, complete_duration)
                i += 1