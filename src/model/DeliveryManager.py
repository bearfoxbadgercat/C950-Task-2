import csv
from datetime import time

from src.model.ChainingHashtable import ChainingHashTable
from src.model.Package import Package
from src.model.Driver import Driver
from src.model.Truck import Truck


class DeliveryManager:
    """
    Class responsible for managing deliveries.
    """

    # Method to populate the driver_hashtable with drivers
    @staticmethod
    def create_driver_hashtable(driver_cht: ChainingHashTable):
        """
        Method to populate the driver_hashtable with drivers
        :param driver_cht: The driver chaining hash table
        :return: None
        """
        for index in range(1, 3):
            key = index
            value = Driver(index, False, None)
            driver_cht.cht_insert(key, value)

    # Method to populate the truck_hashtable with trucks
    @staticmethod
    def create_truck_hashtable(truck_cht: ChainingHashTable):
        """
        Method to populate the truck_hashtable with trucks
        :param truck_cht: The truck chaining hash table
        :return: None
        """
        for i in range(1, 4):
            key = i
            value = Truck(i, None, 0, False, 0, [],
                          None, None, .3)
            truck_cht.cht_insert(key, value)

    @staticmethod
    def create_package_hashtable(package_cht: ChainingHashTable):
        """
        Method to populate the package_hashtable with packages
        :param package_cht: The package chaining hash table
        :return:
        """
        with open('data/package_file.csv', 'r', encoding='utf-8-sig') as file:
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
                status = "At the Hub"
                time_at_hub = time(8, 0)
                time_en_route = None
                time_delivered = None
                truck = None
                delivery_location_id = None
                time_left = None
                distance_to_truck = None
                minute_per_mile = None
                key = package_id
                value = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                                time_at_hub, time_en_route, time_delivered, truck, delivery_location_id, time_left,
                                distance_to_truck, minute_per_mile)
                package_cht.cht_insert(key, value)

    @staticmethod
    def create_distance_table(location_cht: ChainingHashTable):
        """
        Method to create the distance table
        :param location_cht:
        :return:
        """
        with open('data/distance_table.csv', 'r', encoding='utf-8-sig') as file:
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

    @staticmethod
    def create_location_id_table(hashtable):
        """
        This method creates the location id table.
        :param hashtable:
        :return:
        """
        with open('data/distance_table.csv', 'r', encoding='utf-8-sig') as file:
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

    @staticmethod
    def setup_trucks(truck_cht):
        """
        Method to set up the trucks
        :param truck_cht:
        :return:
        """
        # We need to update truck of id 1 in truck_cht to have a departure time of 8:00 AM, which should be a date/time
        # object.
        truck1 = truck_cht.search(1)
        truck2 = truck_cht.search(2)
        truck1.departure_time = time(8, 0)
        truck1.current_time = truck1.departure_time
        truck2.departure_time = time(9, 5)
        truck2.current_time = truck2.departure_time
        truck_cht.cht_insert(1, truck1)
        truck_cht.cht_insert(2, truck2)

    @staticmethod
    def setup_package_information(package_cht, location_id_cht):
        """
        Method to set up the package information
        :param location_id_cht:
        :param package_cht:
        :return:
        """
        # Packages with delivery deadline at 9:00 AM adjust time to time(9, 0)
        package_ids_9am = [15]
        for package_id in package_ids_9am:
            package_cht.search(package_id).deadline = time(9, 0)

        # Packages with delivery deadline at 10:30 AM adjust time to time(10, 30)
        package_ids_1030am = [1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40]
        for package_id in package_ids_1030am:
            package_cht.search(package_id).deadline = time(10, 30)

        # Packages with end of day (EOD) delivery deadline adjust time to time(23, 59)
        package_ids_eod = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 32, 33, 35, 36, 38,
                           39]
        for package_id in package_ids_eod:
            package_cht.search(package_id).deadline = time(23, 59)

        # Packages with delayed arrival time at 09:05 AM
        package_ids_delayed = [6, 25, 28, 32]

        for package_id in package_ids_delayed:
            package_cht.search(package_id).time_at_hub = time(9, 5)

        # Set Time Left which is the minutes between deadline time and arrival time but do it without interation
        package_ids_time_left = range(1, 41)
        for ids in package_ids_time_left:
            package = package_cht.search(ids)
            if package.time_at_hub is not None:
                package.time_left = (package.deadline.hour - package.time_at_hub.hour) * 60 + (
                        package.deadline.minute - package.time_at_hub.minute)
                package_cht.cht_insert(ids, package)

        # Set Location IDs for delivery location
        package_ids_location_id = range(1, 41)
        # We need to get the address and zip code from the package and then use tha
        # t to get the location id from the
        # location_id hashtable
        for ids in package_ids_location_id:
            package = package_cht.search(ids)
            address = package.address
            zip_code = package.zip_code
            key = address + " " + zip_code
            # print(key)
            location_id = location_id_cht.search(key)
            package.delivery_location_id = location_id
            package_cht.cht_insert(ids, package)

        # Set the distance to the delivery location by getting the distance from the location_cht using the location 0
        # and the location id of the delivery location
        range(1, 41)

    @staticmethod
    def set_package_distances(all_packages, distance_table):
        """
        Set the distance from the truck and minute per mile for each package.

        :param all_packages: ChainingHashTable of all packages
        :param distance_table: ChainingHashTable representing the distance table
        """
        for d_id in range(1, 41):
            package = all_packages.search(d_id)
            loc = package.delivery_location_id
            distance = distance_table.search(0).search(loc)
            if distance is None:
                distance = distance_table.search(loc).search(0)
            package.distance_to_delivery = distance
            # Ensure that `time_left` and `distance` are not zero to avoid division by zero error
            if distance and package.time_left:
                package.minute_per_mile = round(float(package.time_left) / float(distance), 0)

    @staticmethod
    # We need a method that assigns a package to a truck and a truck to a package
    def assign_package_to_truck(package, truck, package_cht, truck_cht):
        """
        Method to assign a package to a truck and a truck to a package
        :param package:
        :param truck:
        :param package_cht:
        :param truck_cht:
        :return:
        """
        # Assign the package to the truck

    @staticmethod
    # Method to load packages onto trucks based on notes, there will be 2, so we need to say that it's based on notes
    def load_packages_special_notes(package_cht, truck_cht):
        """
        Method to load packages onto trucks based on notes
        :param package_cht:
        :param truck_cht:

        :return: None
        """
        # Declare the trucks
        truck1 = truck_cht.search(1)
        truck2 = truck_cht.search(2)

        # Load Trucks based on notes
        # Load Truck 1:
        # Packages 13, 14, 15, 16, 19, 20 per the notes
        # Note: Packages must be delivered together
        truck1.delivery_list.append(13)
        truck1.delivery_list.append(14)
        truck1.delivery_list.append(15)
        truck1.delivery_list.append(16)
        truck1.delivery_list.append(19)
        truck1.delivery_list.append(20)

        # Load Truck 2:
        # Part 1: Packages 3, 18, 36 and 38 per the notes
        # Note: Packages must be on Truck 2
        truck2.delivery_list.append(6)
        truck2.delivery_list.append(3)
        truck2.delivery_list.append(18)
        truck2.delivery_list.append(36)
        truck2.delivery_list.append(38)

        # Part 2: Packages 25, 28, 32 per the notes
        # Note: Delayed on flight---will not arrive to depot until 9:05 am
        truck2.delivery_list.append(25)
        truck2.delivery_list.append(28)
        truck2.delivery_list.append(32)

        # Load Truck 3:
        # Package 9 per the notes
        # Note: Wrong address listed for package 9 not updated until 10:20. Ensures delivered to correct address
        truck3 = truck_cht.search(3)
        truck3.delivery_list.append(9)

        #  Package Assignment - Add truck Label to the package
        # Truck 1 Package Assignment
        # Assign 13, 14, 15, 16, 19, 20 to truck 1
        package13 = package_cht.search(13)
        package14 = package_cht.search(14)
        package15 = package_cht.search(15)
        package16 = package_cht.search(16)
        package19 = package_cht.search(19)
        package20 = package_cht.search(20)
        package13.truck = 1
        package14.truck = 1
        package15.truck = 1
        package16.truck = 1
        package19.truck = 1
        package20.truck = 1

        # Truck 2 Package Assignment - Add truck label to the package
        # Assign 3, 18, 36, 38 and 25, 28, 32 with truck 2
        package3 = package_cht.search(3)
        package6 = package_cht.search(6)
        package18 = package_cht.search(18)
        package36 = package_cht.search(36)
        package38 = package_cht.search(38)
        package25 = package_cht.search(25)
        package28 = package_cht.search(28)
        package32 = package_cht.search(32)
        package3.truck = 2
        package6.truck = 2
        package18.truck = 2
        package36.truck = 2
        package38.truck = 2
        package25.truck = 2
        package28.truck = 2
        package32.truck = 2

        # Truck 3 Package Assignment - Adds truck label to the package
        # Assign 9 with truck 3
        package9 = package_cht.search(9)
        package9.truck = 3

    @staticmethod
    # Method to load packages - this is the second step after packages with special notes have been loaded
    def load_packages_standard(package_cht, truck_cht):
        """
        Method to load packages onto trucks based on notes
        :param package_cht:
        :param truck_cht:
        :return:
        """
        #  Step 1: Get the trucks and the remaining packages to work with
        #  Trucks
        truck1 = truck_cht.search(1)
        truck2 = truck_cht.search(2)
        truck3 = truck_cht.search(3)

        #  Remaining Packages
        remaining_packages = []
        express_remaining_packages = []
        for i in range(1, 41):
            package = package_cht.search(i)
            if package.truck is None:
                if package.deadline != time(23, 59):
                    express_remaining_packages.append(package)
                    package.truck = 1
                else:
                    remaining_packages.append(package)

        # Load express packages
        while len(express_remaining_packages) > 0:
            if len(truck1.delivery_list) < 16:
                truck1.delivery_list.append(express_remaining_packages[0].package_id)
                express_remaining_packages[0].truck = 1
                express_remaining_packages.pop(0)
        # Load remaining packages, we'll need to
        while len(remaining_packages) > 0:
            if len(truck1.delivery_list) < 16:
                truck1.delivery_list.append(remaining_packages[0].package_id)
                remaining_packages[0].truck = 1
                remaining_packages.pop(0)
            elif len(truck2.delivery_list) < 16:
                truck2.delivery_list.append(remaining_packages[0].package_id)
                remaining_packages[0].truck = 2
                remaining_packages.pop(0)
            elif len(truck3.delivery_list) < 16:
                truck3.delivery_list.append(remaining_packages[0].package_id)
                remaining_packages[0].truck = 3
                remaining_packages.pop(0)

    @staticmethod
    def setup_environment(driver_cht: ChainingHashTable, truck_cht: ChainingHashTable,
                          package_cht: ChainingHashTable, location_cht: ChainingHashTable,
                          location_id_cht: ChainingHashTable, distance_table_cht: ChainingHashTable):
        """
        Method to set up the WGUPS environment
        :param driver_cht: The driver chaining hash table
        :param truck_cht: The truck chaining hash table
        :param package_cht: The package chaining hash table
        :param location_cht: The location chaining hash table
        :param location_id_cht: The location id chaining hash table
        :param distance_table_cht: The distance table chaining hash table
        :return: None
        """
        # Create Hashtable
        DeliveryManager.create_driver_hashtable(driver_cht)  # Populate the driver hashtable
        DeliveryManager.create_truck_hashtable(truck_cht)  # Populate the truck hashtable
        DeliveryManager.create_package_hashtable(package_cht)  # Populate the package hashtable
        DeliveryManager.create_distance_table(location_cht)  # Populate the distance table
        DeliveryManager.create_location_id_table(location_id_cht)  # Populate the location id table

        # Initialize the WGUPS environment
        DeliveryManager.setup_trucks(truck_cht)  # Set up initial truck states
        DeliveryManager.setup_package_information(package_cht, location_id_cht)  # Set up initial driver states
        DeliveryManager.set_package_distances(package_cht, distance_table_cht)  # Set up package distances
        DeliveryManager.load_packages_special_notes(package_cht, truck_cht)
        DeliveryManager.load_packages_standard(package_cht, truck_cht)

    @staticmethod
    def change_driver_status():
        pass

    @staticmethod
    def ath_packages_to_deliver(truck_cht: ChainingHashTable):
        """
        Procedure to check if there are packages At The Hub that still need to be delivered
        :return: Number of packages at the hub that still need to be delivered
        """
        remaining_packages_ATH = 0  # Number of packages at the hub that still need to be delivered
        for truck in range(1, 4):
            remaining_packages_ATH += len(truck_cht.search(truck).delivery_list)
        return int(remaining_packages_ATH)

    @staticmethod
    def assign_driver_to_truck(driver_id, truck_id, drivers, trucks):
        """
        Method to assign a driver to a truck
        :param driver_id:
        :param truck_id:
        :param drivers:
        :param trucks:
        :return:
        """
        trucks.search(truck_id).truck_driver = drivers.search(driver_id).driver_id
        drivers.search(driver_id).assigned_truck = trucks.search(truck_id).truck_id
        trucks.search(truck_id).truck_status = True
        drivers.search(driver_id).status_active = True

    @staticmethod
    def unassign_driver_from_truck(driver_id, truck_id, drivers, trucks):
        """
        Method to unassign a driver from a truck
        :param driver_id:
        :param truck_id:
        :param drivers:
        :param trucks:
        :return:
        """
        trucks.search(truck_id).truck_driver = None
        drivers.search(driver_id).assigned_truck = None
        trucks.search(truck_id).truck_status = False
        drivers.search(driver_id).status_active = False
