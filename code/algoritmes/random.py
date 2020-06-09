import random

# Globaal idee van het random algoritme: 

def random_start(self, trajects, stations):
    """ kiest een random startplek voor alle trajecten (input lijst van trajecten [1 to 7 bijv.]) """"
    for traject in trajects:
        traject.current_station = random.choice(stations)

def add_random_connection(self, current_station)
    """ vanaf de current_station van de trein, kiest hij een random connectie en voegt hij toe aan zijn traject"""
    trajects.append(random.choice(current_station.get.connection()))

# Nog toevoegen:

# available_connections (traject.py)
# stop conditie (traject.py)
# daarna kijken naar aantal trajecten (dus niet per se 7)


