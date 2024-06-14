#!/usr/bin/python3

import csv
import json

"""
converts csv into json
"""


def convert_csv_to_json(csv_filename):
    """
    converst csv to json
    Attributes:
        csv_filename: file to convert to json
    """
    try:
        with open(csv_filename, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
        
        json_filename = 'data.json'
        with open(json_filename, mode='w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Data from {csv_filename} has been converted to {json_filename}")
        return True
    
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
