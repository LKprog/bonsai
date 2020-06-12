class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connections = []
        self.unused_connections = []

    def connection(self, next_station, duration):
        self.connections.append([next_station, duration])

    def connections_list(self):
        return self.connections

    def add_unused_connection(self, next_station, duration):
        self.unused_connections.append([next_station, duration])

    def __repr__(self):
        return self.name
        # f"Name: {self.name}, Connections: {self.connections}"