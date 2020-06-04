class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connections = {}

    # def add_connection(self, end_station, duration):
    #     self.connections[station.name] = end_station
    #     self.connections[station.name] = duration

    def __repr__(self):
        return f"Name: {self.name}, x= {self.x}, y= {self.y}"