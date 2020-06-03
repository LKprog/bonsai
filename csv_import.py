import csv

class station():

    def__init__(self, station, x, y):
        self._station = station
        self._x = x
        self._y = y

        f = open("StationsHolland.csv")
        stations = csv.reader(f)

class connection():
    
    def__init__(self, station1, station2, duration):
        self._station1 = station1
        self._station2 = station2
        self._duration = duration

    f = open("ConnectiesHolland.csv")
    connecties = csv.reader(f)