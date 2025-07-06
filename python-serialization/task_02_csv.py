#!/usr/bin/python3
# """Defines function that converts csv to json"""

import csv
import json

def convert_csv_to_json(csv_file):
    """Function writes data to data.json
    Args:
    csv_file: csv file to convert
    data.json: json file to write to
    """
    try:
        with open(csv_file "r") as csv_f:
            data = csv.DictReader(csv_f)
            for line in data:
                print(line)
    except Exception:
        return False

    try:
        with open("data.json", "w") as dj_f:
            json.dump(data, dj_f)
        return True
    except FileNotFoundError:
        return False
