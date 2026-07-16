#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Invalid input: Template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    file_number = 1

    for attendent in attendees:
        for key, value in attendent.items():
            if value is None or str(value).strip() == "":
                attendent[key] = "N/A"
        
        template_copy = template
        template_copy = template_copy.replace("{name}", attendent.get("name", "N/A"))
        template_copy = template_copy.replace("{event_title}", attendent.get("event_title", "N/A"))
        template_copy = template_copy.replace("{event_date}", attendent.get("event_date", "N/A"))
        template_copy = template_copy.replace("{event_location}", attendent.get("event_location", "N/A"))
        
        filename = f"output_{file_number}.txt"
        if os.path.exists(filename):
            print(f"File {filename} already exists.")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                    f.write(template_copy)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
        file_number += 1