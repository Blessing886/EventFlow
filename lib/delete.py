from models.events import Event

Event.create_table()

Event.delete_all()
print(f"all events deleted")