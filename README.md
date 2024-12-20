# EVENTFLOW

#### By
-- Blessing Okora

## Overview

The **EventFlow** is an event management command-line application designed to hep users manage
events and attendees. Users can create, view, update and delete events and attendees in a
SQLite database. The system also allows retrival of attendees for specific events and
searching for events by date.

## Features
### Event Management
- Create new event.
- View all events.
- Search event by ID.
- Search event by date.
- Update an event's details.
- Delete an event.

### Attendee Management
- Create a new attendee.
- View all attendees.
- Find attendees of a specific event.
- Update an attendees details.
- Delete an attendee.

## Project Structure

|---lib
        |--__pycache__
        |--models
                |--__init__.py
                |--atttendees.py
                |--events.py
                |--eventflow.db
        |--cli.py
        |--debug.py
        |--helpers.py
        |run_db.py  
|---LICENCE
|---pipfile
|---pipfile.lock
|---README.md  

## Technologies Used
-**Python**
-**SQL**

## Getting Started

### Prerequisites
- Python 3.8 or higher
- SQLite

### Installation
1. Clone the repository:https://github.com/Blessing886/EventFlow.git
2. Navigate into the "EventFlow" directory
3. Run `lib/run_db.py` to trigger dabase connection and create eventflow.db

## Usage

### Running the CLI
- Run `python lib/cli.py` to run the application from the terminal.
### Menu Options
0. Exit the program.
1. View all events.
2. Find event by date.
3. Find event by ID.
4. Create event.
5. Update event.
6. Delete event.
7. Create an attendee.
8. View all attendees.
9. Find attendees of an event.
10. Update an attendee.
11. Delete an attendee.

#### Examples
##### Create an event
- Select option 4 from the menu.
- Enter the enter the event name, press enter, enter the event date, press enter then
finally the event location.
- The event will be saved in the database.

##### Find attendees of an event
- Select option 9 from the menu.
- Enter the event ID.
- A list from that event will be displayed.

** To exit the program enter 0**

## Testing
- Run `python lib/debug.py` to test the application. A series of print texts will be
generated in the terminal showing the process of CRUD operations.

## Future Enhancements
- Add other operations such as search by event name and search by attendee name.
- Add automated tests for CRUD operations.

## Support and Contact Details
- Email: <moraablessing082@gmail.com>

## LICENCE
MIT License

Copyright (c) 2024 Blessing Okora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
