import csv

from src.model.ChainingHashtable import ChainingHashTable
from src.model.Package import Package


def number_of_packages():
    with (open('package_file.csv', 'r', encoding='utf-8-sig') as file):
        reader = csv.reader(file)
        number_packages = len(list(reader))
    return number_packages


package_hashtable = ChainingHashTable(number_of_packages())

with open('package_file.csv', 'r', encoding='utf-8-sig') as file2:
    reader2 = csv.reader(file2)
    for index, row in enumerate(reader2):
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        status = ""
        time_at_hub = ""
        time_en_route = ""
        time_delivered = ""
        truck = ""
        delivery_location_id = ""
        time_left = ""
        distance_to_truck = ""
        minute_per_mile = ""
        key = package_id
        value = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status, time_at_hub,
                        time_en_route, time_delivered, truck, delivery_location_id, time_left, distance_to_truck,
                        minute_per_mile)
        package_hashtable.cht_insert(key, value)



# Method to set the delivery_location_id for all packages. To do this we need the address and zip code.
# We need to reference the location_id_hashtable to get the delivery_location_id.  It will use the address and zip code
# as the key to get the value and set the delivery_location_id for the package to that value.
def set_delivery_location_id(pht, lht):
    with open('package_file.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            address = row[1]
            zip_code = row[4]
            key = address + " " + zip_code
            value = lht.search(key)
            package_id = int(row[0])
            package = pht.search(package_id)
            package.delivery_location_id = value

package_hashtable.print_all_values()