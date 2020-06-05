class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connections = []

    def add_connection(self, end_station, duration):
        self.connections.append(f'{end_station}, {duration}')

    def connections_list(self):
        return self.connections

    def __repr__(self):
        return f"Name: {self.name}, Connections: {self.connections}"