# This code reads the CSV for the distance table and makes it searchable.

import csv

from src.model.ChainingHashtable import ChainingHashTable


# Let's create an __init__method method that will establish the distance table

def create_distance_table(hashtable):
    with open('distance_table.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # Continue with your code

        # Here we are going through each row and noting the index as the key and the value as the ChainingHashTable
        for row_index, row in enumerate(reader):
            key = row_index
            distance_hashtable = ChainingHashTable(
                27)  # Assuming 27 is the maximum number of columns including the first key column
            value = distance_hashtable
            hashtable.cht_insert(key, value)
            for column_index in range(1, len(row)):
                if row[column_index]:  # Check if the cell is not empty
                    subkey = column_index - 1
                    subvalue = row[column_index]
                    value.cht_insert(subkey, subvalue)
    return hashtable


def distance_between_locations(lht):
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


def main():
    create_distance_table()
