#!/usr/bin/env python3
from os.path import exists
#Program defines function that generates personalized invitation files

def generate_invitations(template,attendees):
    if not isinstance(template, str) or not template:
        print("Template is empty, no output files generated.")
        return

    if not isinstance(attendees,list) or not  attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees,1):
        message=template
        fields = ["name", "event_title", "event_date", "event_location"]
        for field in fields:
            value = attendee.get(field)   
            if value is None:
                value = "N/A"
            message = message.replace(f"{{{field}}}", value)

        filename = f"output_{index}.txt"
        if not exists(filename):
            with open(filename, "w") as file:
                file.write(message)
        else:
            print(f"ERROR: {filename} already exists")

if __name__ == "__main__":
    template = "Dear {name},\nYou are invited to {event_title} on {event_date} at {event_location}.\n"
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2025-08-01", "event_location": "Baku"},
        {"name": "Bob", "event_title": "AI Summit", "event_date": "2025-08-05", "event_location": "Ganja"},
        {"name": "Charlie", "event_title": "Hackathon", "event_date": "2025-08-10", "event_location": "Sumgait"},
    ]
    generate_invitations(template, attendees)
