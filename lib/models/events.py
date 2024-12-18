from . import CONN, cursor

class Event:
    def __init__(self, name, date, location, id=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location