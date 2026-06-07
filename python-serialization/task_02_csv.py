#!/usr/bin/python3


import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        with open("data.json", 'w', encoding="utf-8") as dj:
            return json.dump(data, dj, indent=4)
        return True
    except Exception:
        return False
