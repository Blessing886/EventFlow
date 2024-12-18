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

    @classmethod
    def create_table(cls):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            event_id INTEGER NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id) ON DELETE CASCADE
            )
        ''')
        CONN.commit()

    def save(self):
        cursor.execute('''
        INSERT INTO attendees (name, email, event_id)
        VALUES (?, ?, ?)
        ''', (self.name, self.email, self.event_id))
        CONN.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_by_id(cls, id):
        cursor.execute('SELECT * FROM attendees WHERE id = ?', (id,))
        row = cursor.fetchone()
        return cls(id=row[0], name=row[1], email=row[2], event_id=row[3]) if row else None
    @classmethod
    def get_by_event_id(cls, event_id):
        cursor.execute('SELECT * FROM attendees WHERE event_id = ?', (event_id,))
        rows = cursor.fetchall()
        return [cls(id=row[0], name=row[1], email=row[2], event_id=row[3]) for row in rows]

        