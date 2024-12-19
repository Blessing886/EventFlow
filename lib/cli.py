from helpers import (
    exit_program,
    view_all_events,
    find_event_by_date,
    find_event_by_id,
    create_event,
    update_event,
    delete_event,
    create_an_attendee,
    view_all_attendees,
    find_attendees_of_an_event,
    update_an_attendee,
    delete_an_attendee,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_events()
        elif choice == "2":
            find_event_by_date()
        elif choice == "3":
            find_event_by_id()
        elif choice == "4":
            create_event()
        elif choice == "5":
            update_event()
        elif choice == "6":
            delete_event()
        elif choice == "7":
            create_an_attendee()
        elif choice == "8":
            view_all_attendees()
        elif choice == "9":
            find_attendees_of_an_event()
        elif choice == "10":
            update_an_attendee()
        elif choice == "11":
            delete_an_attendee()
        else:
            print("Invalid Choice!")

def menu():
    print("\nEvent Management System")
    print("*************************")
    print("Please select an option:")
    print("0.Exit the program")
    print("1.View all events")
    print("2.Find event by date")
    print("3.Find event by ID")
    print("4.Create event")
    print("5.Update event")
    print("6.Delete event")
    print("7.Create an attendee")
    print("8.View all attendees")
    print("9.Find attendees of an event")
    print("10.Update an attendee")
    print("11.Delete an attendee")

if __name__ == "__main__":
    main()