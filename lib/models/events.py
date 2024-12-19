from . import CONN, cursor

class Event:
    def __init__(self, name, date, location, id=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', date='{self.date}', location='{self.location}')"

    @classmethod
    def create_table(cls):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                location TEXT
            )
        ''')
        CONN.commit()

    def save(self):
        cursor.execute('''
            INSERT INTO events (name, date, location)
            VALUES (?, ?, ?)
        ''', (self.name, self.date, self.location))
        CONN.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_by_id(cls, id):
        cursor.execute('SELECT * FROM events WHERE id = ?', (id,))
        row = cursor.fetchone()
        return cls(id=row[0], name=row[1], date=row[2], location=row[3]) if row else None
    
    @classmethod
    def get_by_date(cls, date):
        cursor.execute('SELECT * FROM events WHERE date = ?', (date,))
        rows = cursor.fetchall()
        return [cls(id=row[0], name=row[1], date=row[2], location=row[3]) for row in rows]
    
    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM events')
        rows = cursor.fetchall()
        return [cls(id=row[0], name=row[1], date=row[2], location=row[3]) for row in rows]
    
    
    def update(self):
        cursor.execute('''
            UPDATE events
            SET name = ?, date = ?, location = ?
            WHERE id = ?
        ''', (self.name, self.date, self.location, self.id))
        CONN.commit()

    def delete(self):
        cursor.execute('DELETE FROM events WHERE id = ?', (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def delete_all(cls):
        cursor.execute('DELETE FROM events')
        CONN.commit()
        