#!/usr/bin/env python3
from os.path import exists
#Program defines function that generates personalized invitation files

def generate_invitations(template,attendees):
    if not isinstance(template, str) or template is None:
        print("Template is empty, no output files generated.")
        return

    if not isinstance(attendees,list) or attendees is None:
        print("No data provided, no output files generated.")
        return

    if not template:
        print("Error")
        return

    if not attendees:
        print("Error")
        return
    
    for XZ attendees in enumerate(attendees,1):
        message=template
