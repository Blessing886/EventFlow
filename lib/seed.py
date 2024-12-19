from models.events import Event
from models.attendees import Attendee

Event.create_table()
Attendee.create_table()
"""create event"""
event = Event(name="Tech Conference", date="2024-12-20", location="Pride Inn, Shanzu")
event.save()
print(f"Created Event: {event}")
event = Event(name="AI Workshop", date="2024-12-21", location="English Point, Mombasa")
event.save()
print(f"Created Event: {event}")

"""get all"""
all_events = Event.get_all()
print(f"all events:")
for event in all_events:
    print(event)

"""get by id"""
event_by_id = Event.get_by_id(event.id)
print(f"event by id retreived: {event_by_id}")

"""update"""
event.name = "updated Tech Conference"
event.update()
print(f"updated Event: {event}")

event.delete()
print(f"event deleted: {event.id}")

"""ATTENDEES"""

print("Events:")
all_events = Event.get_all()
for event in all_events:
    print(event)

select_event_id = int(input("Enter event id: "))
existing_event = Event.get_by_id(select_event_id)

"""create attendee"""
attendee = Attendee(name="Blessing Okora", email="blessing@gmail.com", event_id=existing_event.id)
attendee.save()
print(f"Created attendee: {attendee}")

"""get all"""
print("all attendees:")
all_attendees = Attendee.get_all()
for attend in all_attendees:
    print(attend)

"""get by id"""
attendee_by_id = Attendee.get_by_id(attendee.id)
print(f"attendee retrieved: {attendee_by_id}")

"""update"""
attendee.name = "Tina Okoth"
attendee.email = "tina@gmail.com"
attendee.update()
print(f"attendee updated: {attendee}")

"""delete"""
attendee.delete()
print(f"deleted attendee with id: {attendee.id}")
 
print("Attendees deleted")
attendees_deleted = Attendee.get_all()
for attend in attendees_deleted:
    print(attend)

