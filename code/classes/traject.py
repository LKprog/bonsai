from .station import Station

class Traject():
    def __init__(self, traject_id, current_station):
        self.traject_id = traject_id
        self.current_station = current_station
        self.trajects = []
        self.trajects.append(current_station)
        self.total_distance = 0

    def get_connection(self, current_station):
        return self.current_station.connections_list

    def add_connection(self, next_station):
        self.trajects.append(next_station[0])
        self.total_distance += next_station[1]
        self.current_station = next_station[0]

    def __repr__(self):
        return str(self.trajects)
    #def stop(self):
        #for traject in self.trajects:
            #if traject
