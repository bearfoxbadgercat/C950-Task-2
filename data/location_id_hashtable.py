# The number of locations is = to the number of rows in the file
# Read in the data from the file and store it into the hashtable
import csv
from src.model.ChainingHashtable import ChainingHashTable


def number_of_location():
    with open('distance_table.csv', 'r') as file1:
        reader1 = csv.reader(file1)
        number_of_locations = len(list(reader1))
    return number_of_locations


location_id_hashtable = ChainingHashTable(number_of_location())


def create_location_id_hashtable(hashtable):
    with open('distance_table.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):  # This will give you the index of each row
            address = row[0].split('(')[0].strip()  # Also added strip() to remove any leading/trailing spaces
            if address == "HUB":
                zip_code = ""
            else:
                try:  # Try to split and catch exception if it fails
                    zip_code = row[0].split('(')[1].split(')')[0]
                except IndexError:  # Handle the case where the split does not work
                    zip_code = ""  # Assign a default value or handle appropriately
            key = address + " " + zip_code
            value = index  # This will assign the current row's index to value
            hashtable.cht_insert(key, value)

create_location_id_hashtable(location_id_hashtable)
location_id_hashtable.get_all()


