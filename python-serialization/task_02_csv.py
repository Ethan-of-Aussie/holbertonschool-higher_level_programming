#!/usr/bin/python3


import csv
import json

def convert_csv_to_json(filename):
    try:
        data = []
        with open(filename, 'r', encoding="utf-8") as f:
            read = csv.DictReader(f)
            for row in read:
                data.append(row)

        with open("data.json", 'w', encoding="utf-8") as dj:
            return json.dump(data, dj)
        return True
    except FileNotFoundError:
        return False
