from models.events import Event
from models.attendees import Attendee

def exit_program():
    print("Goodbye!")
    exit()

# Event functions
def view_all_events():
    event = Event.get_all()
    for event in event:
        print(event)

def find_event_by_date():
    try:
        date = input("Enter the event date (YYYY-MM-DD): ")
        events = Event.get_by_date(date)
        if events:
            print(f"Events on {date}:")
            for event in events:
                print(event)
        else:
            print(f"No events found on {date}.")
    except Exception as err:
        print(f"An error occurred: {err}")

def find_event_by_id():
    id_ = input("Enter the event's ID: ")
    event = Event.get_by_id(id_)
    print(event) if event else print(f"Event ID '{id_}' not found.")

def create_event():
    try:
        name = input("Enter the event name: ")
        date = input("Enter the event date (YYYY-MM-DD): ")
        location = input("Enter event location: ")

        event = Event(name=name, date=date, location=location)
        event.save()
        print(f"Event '{event.name}' successfully created with ID: {event.id}.")
    except Exception as err:
        print(f"An error occurred while creating the event: {err}")


def update_event():
    pass

def delete_event():
    id_ = input("Enter event's ID: ")
    event = Event.get_by_id(id_)
    if event:
        event.delete()
        print(f"Event ID '{id_}' deleted successfully.")
    else:
        print(f"Event ID '{id_}' not found.")

# Attendee functions