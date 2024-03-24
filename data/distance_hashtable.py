# This code reads the CSV for the distance table and makes it searchable.

import csv

from src.model.ChainingHashtable import ChainingHashTable

locations_hashtable = ChainingHashTable(27)  # 27 is the number of rows in the file


def __init__(self):
    pass


def create_distance_table(location_cht: ChainingHashTable):
    with open('distance_table.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # Continue with your code

        # Here we are going through each5 row and noting the index as the key and the value as the ChainingHashTable
        for row_index, row in enumerate(reader):
            key = row_index
            distance_hashtable = ChainingHashTable(27)
            value = distance_hashtable
            location_cht.cht_insert(key, value)
            for column_index in range(1, len(row)):
                if row[column_index]:  # Check if the cell is not empty
                    subkey = column_index - 1
                    subvalue = row[column_index]
                    value.cht_insert(subkey, subvalue)


def distance_between_locations(lht: ChainingHashTable):
    # Let's ask the user for the row which is asking what location we are starting at. We'll do this by asking for the
    # user's input and then searching the location
    first_location = int(input("What is the first location? "))
    second_location = int(input("What is the second location? "))

    row_hashtable = lht.search(first_location)
    distance = row_hashtable.search(second_location)
    try:
        if distance is None:
            row_hashtable = locations_hashtable.search(second_location)
            distance = row_hashtable.search(first_location)
            return distance
        else:
            return distance
    except AttributeError:
        return "Invalid locations. Please try again."



create_distance_table(locations_hashtable)
print(distance_between_locations(locations_hashtable))
