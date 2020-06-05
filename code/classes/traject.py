from station import Station

class Traject():
    def __init__(self, traject_id, current_station):
        self.traject_id = traject_id
        self.current_station = current_station
        self.trajects = []
        self.total_distance = 
        
    def get_connection(self, current_station):
        return self.connections_list.get(current_station)

    def add_connection(self, next_station):
        self.traject.append(next_station[0])
        self.total_distance += next_station[1]
    
    def move(self):
        self.current_station = self.next_station

    def stop(self):
        for traject in self.trajects:
            if traject

