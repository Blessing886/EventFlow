from models.events import Event
from models.attendees import Attendee

Event.create_table()


'''
Event.delete_all()
print(f"all events deleted")
'''

print("All attendees:")
all_attendees = Attendee.get_all()
for attend in all_attendees:
    print(attend)

Attendee_id_delete = int(input("Enter id: "))
Attendee = Attendee.get_by_id(Attendee_id_delete)
Attendee.delete()
print(f"Deleted attendee with id: {Attendee_id_delete}")

print("Attendees available:")
Attendees_after_deletion = Attendee.get_all()
for attend in Attendees_after_deletion:
    print(attend)