import csv

from src.model.ChainingHashtable import ChainingHashTable
from src.model.Package import Package
from pathlib import Path


class PackageData:
    """
    This class is used to create a hashtable for the packages.
    """

    def __init__(self):
        """
        This method initializes the hashtable.
        """
        self.package_table = None
        self.hashtable = ChainingHashTable(40)

    def create_package_table(self):
        """
        This method creates the package hashtable.
        :return: hashtable of packages
        """
        csv_file = Path('C:/Users/Mikie/PycharmProjects/C950 Task 2/data/package_file.csv')
        with csv_file.open('r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                deadline = row[5]
                weight = row[6]
                notes = row[7]
                status = None
                time_at_hub = None
                time_en_route = None
                time_delivered = None
                truck = None
                delivery_location_id = None
                time_left = None
                distance_to_truck = None
                minute_per_mile = None
                key = package_id
                value = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                                time_at_hub,
                                time_en_route, time_delivered, truck, delivery_location_id, time_left,
                                distance_to_truck,
                                minute_per_mile)
                self.hashtable.cht_insert(key, value)
        return self.hashtable


    def set_location_id(self):
        """
        This method sets the delivery location id for all the packages.
        :return: delivery location id
        """
        # This method sets the delivery_location_id for all packages. To do this we will need to reference the
        # all_packages hashtable to get the package.  For each package we will get the address and zip code.




def main():
    """
    This method is used to test the package hashtable.
    """
    all_packages = PackageData()
    all_packages.create_package_table()
    print(all_packages.print_all_packages())


if __name__ == '__main__':
    main()
