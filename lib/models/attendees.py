from . import CONN, cursor

class Attendee:
    def __init__(self, name, email, event_id, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.event_id = event_id

    def __repr__(self):
        return f"Attendee(id={self.id}, name='{self.name}', email='{self.email}',
        event_id={self.event_id})"
    
    

        