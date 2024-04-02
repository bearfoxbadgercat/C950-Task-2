import csv
from datetime import datetime, time, timedelta
from src.model.ChainingHashtable import ChainingHashTable
from src.model.Driver import Driver
from src.model.Package import Package

from src.model.Truck import Truck


class NewDeliveryManager:
    """
    This class is used to manage the delivery environment
    """
    trucks: list[Truck | None]

    def __init__(self):
        """
        Constructor for the NewDeliveryManager
        """
        # List of trucks
        self.trucks = [None,
                       Truck(truck_id=1, truck_driver=1, truck_location=0, truck_status=False, truck_mileage=0,
                             delivery_list=[], departure_time=time(8, 0),
                             current_time=time(8, 0), return_time=None, speed=18.0),  # Truck 1
                       Truck(truck_id=2, truck_driver=2, truck_location=0, truck_status="Inactive", truck_mileage=0,
                             delivery_list=[], departure_time=time(9, 5),
                             current_time=time(0, 0), return_time=None, speed=18.0),  # Truck 2
                       Truck(truck_id=3, truck_driver=3, truck_location=0, truck_status="Inactive", truck_mileage=0,
                             delivery_list=[], departure_time=time(8, 0),
                             current_time=time(0, 0), return_time=None, speed=18.0)]  # Truck 3

        # List of drivers
        self.drivers = [Driver(driver_id=1, status_active=True, assigned_truck=1),
                        Driver(driver_id=2, status_active=True, assigned_truck=2), ]

        # List of packages
        self.all_packages = ChainingHashTable(40)

        # Distance table
        self.distance_table = ChainingHashTable(27)  # Location Table

        # Location ID
        self.location_id_table = ChainingHashTable(27)  # Location ID

        # Total miles
        self.total_miles = 0

    """Procedures: Populate Data Structures with Initial Data"""

    @staticmethod
    def get_user_time():
        while True:
            try:
                hour = int(input("Please enter the hour (0-23): "))
                if hour < 0 or hour > 23:
                    raise ValueError("Hour must be between 0 and 23.")
                minute = int(input("Please enter the minute (0-59): "))
                if minute < 0 or minute > 59:
                    raise ValueError("Minute must be between 0 and 59.")
                formatted_time = datetime.strptime(f"{hour:02d}:{minute:02d}", "%H:%M").time()
                return formatted_time
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_user_input(user_package_id, user_time):
        try:
            print("You  entered: ", user_package_id, " at ", user_time, ".")
            # Ask if this is correct as an input.
            # If the user says no, then we will ask for the values again.
            # If the user says yes, then we will continue with the program.
            if input("Is this correct? (Y/N): ").lower() == "n":
                user_package_id = input("Enter the package ID: ")
                user_time = NewDeliveryManager.get_user_time()
                NewDeliveryManager.validate_user_input(user_package_id, user_time)
        except ValueError as e:
            print(e)

    def populate_packages(self):
        """
        Procedure to populate the packages hashtable
        :return: None
        """
        with open('data/package_file.csv', 'r',
                  encoding='utf-8-sig') as file:
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
                status = "At The Hub"
                time_at_hub = ""
                time_en_route = ""
                time_delivered = ""
                truck = ""
                delivery_location_id = ""
                time_left = ""
                distance_to_truck = ""
                minute_per_mile = ""
                key = package_id
                value = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                                time_at_hub,
                                time_en_route, time_delivered, truck, delivery_location_id, time_left,
                                distance_to_truck,
                                minute_per_mile)
                self.all_packages.cht_insert(key, value)

    def populate_distance_table(self):
        """
        Procedure to populate the distance table
        :return: None
        """
        with open(r'data/distance_table.csv', 'r',
                  encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            # Continue with your code

            # Here we are going through each5 row and noting the index as the key and the value as the ChainingHashTable
            for row_index, row in enumerate(reader):
                key = row_index
                distance_hashtable = ChainingHashTable(27)
                value = distance_hashtable
                self.distance_table.cht_insert(key, value)
                for column_index in range(1, len(row)):
                    if row[column_index]:  # Check if the cell is not empty
                        subkey = column_index - 1
                        subvalue = row[column_index]
                        value.cht_insert(subkey, subvalue)

    def populate_location_id_table(self):
        """
        This procedure creates the location id table.
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
                self.location_id_table.cht_insert(key, value)

    """Procedure: Initialize Delivery Environment"""

    # Set Package Initial Status
    def set_package_status(self, package_id, status):
        """
        Procedure to set the status of a package
        :param package_id:
        :param status:
        :return:
        """
        self.all_packages.search(package_id).status = status

    def set_package_time_at_hub(self):
        """
        Procedure to set the time at the hub for a package
        :return:
        """
        for i in range(1, 41):
            if i not in [6, 25, 28, 32]:
                self.all_packages.search(i).time_at_hub = time(8, 0)
            else:
                self.all_packages.search(i).time_at_hub = time(9, 5)

    def assign_truck_to_package(self, package_id, truck_id):
        """
        Procedure to assign a truck to a package
        :param package_id:
        :param truck_id:
        :return:
        """
        self.all_packages.search(package_id).truck = truck_id

    def add_truck_label_to_packages(self):
        """
        Procedure to add a truck label to the package
        :return:
        """

        # Truck 1 Assignment
        self.assign_truck_to_package(1, 1)
        self.assign_truck_to_package(13, 1)
        self.assign_truck_to_package(14, 1)
        self.assign_truck_to_package(15, 1)
        self.assign_truck_to_package(16, 1)

        self.assign_truck_to_package(19, 1)
        self.assign_truck_to_package(20, 1)
        self.assign_truck_to_package(29, 1)
        self.assign_truck_to_package(30, 1)
        self.assign_truck_to_package(31, 1)

        self.assign_truck_to_package(34, 1)
        self.assign_truck_to_package(37, 1)
        self.assign_truck_to_package(40, 1)
        # Total assigned to 1: 13

        # Truck 2 Assignment
        self.assign_truck_to_package(3, 2)
        self.assign_truck_to_package(6, 2)
        self.assign_truck_to_package(18, 2)
        self.assign_truck_to_package(25, 2)
        self.assign_truck_to_package(28, 2)

        self.assign_truck_to_package(32, 2)
        self.assign_truck_to_package(36, 2)
        self.assign_truck_to_package(38, 2)
        self.assign_truck_to_package(33, 2)
        self.assign_truck_to_package(35, 2)

        self.assign_truck_to_package(39, 2)
        # Total assigned to 2: 11

        # Assign truck 3 to packages that need to go on truck 3 (9)

        # Truck 3 Assignment
        self.assign_truck_to_package(2, 3)
        self.assign_truck_to_package(4, 3)
        self.assign_truck_to_package(5, 3)
        self.assign_truck_to_package(7, 3)
        self.assign_truck_to_package(8, 3)

        self.assign_truck_to_package(9, 3)
        self.assign_truck_to_package(10, 3)
        self.assign_truck_to_package(11, 3)
        self.assign_truck_to_package(12, 3)
        self.assign_truck_to_package(17, 3)

        self.assign_truck_to_package(21, 3)
        self.assign_truck_to_package(22, 3)
        self.assign_truck_to_package(23, 3)
        self.assign_truck_to_package(24, 3)
        self.assign_truck_to_package(26, 3)

        self.assign_truck_to_package(27, 3)
        # Total assigned to 3: 16

    def set_initial_distances(self, truck_location):
        for i in range(1, 41):
            self.all_packages.search(i).distance = self.get_distance(truck_location,
                                                                     self.all_packages.search(i).delivery_location_id)

    def set_time_en_route(self):
        for i in range(1, 41):
            if self.all_packages.search(i).truck == 1:
                self.all_packages.search(i).time_en_route = time(8, 0)
            elif self.all_packages.search(i).truck == 2:
                self.all_packages.search(i).time_en_route = time(9, 5)
            else:
                self.all_packages.search(i).time_en_route = None

    def set_deadline(self):
        for i in range(1, 41):
            package = self.all_packages.search(i)  # Get the package once per loop
            if package.deadline == "9:00 AM":
                package.deadline = time(9, 0)
            if package.deadline == "10:30 AM":
                package.deadline = time(10, 30)
            if package.deadline == "EOD":
                package.deadline = time(23, 59)

    def load_packages(self):
        """
        Method to load the packages
        :return:
        """
        # We do this by reading the assigned truck for each package and adding it to the delivery list of the truck
        for i in range(1, 41):
            if self.all_packages.search(i).truck == 1:
                self.trucks[1].delivery_list.append(i)
            elif self.all_packages.search(i).truck == 2:
                self.trucks[2].delivery_list.append(i)
            else:
                self.trucks[3].delivery_list.append(i)

    """Methods to return relevant information about the delivery environment."""

    def get_distance(self, location1, location2):
        """
        Method to get the distance between two locations
        :param location1:
        :param location2:
        :return: distance between location1 and location2
        """
        distance = self.distance_table.search(location1).search(location2)
        if distance is None:
            distance = self.distance_table.search(location2).search(location1)
            return distance
        else:
            return distance

    def set_location_id(self):
        """
        Method to assign the location id to the packages
        :return: location id
        """
        for ids in range(1, 41):
            address = self.all_packages.search(ids).address
            zip_code = self.all_packages.search(ids).zip_code
            key = address + " " + zip_code
            value = self.location_id_table.get_value(key)
            self.all_packages.search(ids).delivery_location_id = value

    def calculate_minute_per_mile(self, package_id):
        """
        Procedure to set the minute per mile for the packages
        :return:
        """
        # this is time in minutes/distance
        package = self.all_packages.search(package_id)
        distance = float(package.distance)
        speed = float(self.trucks[package.truck].speed / 60)

        minute_per_mile = distance / speed
        return int(minute_per_mile)

    def calculate_time_left(self, pid: int):
        """
        Method to calculate the time left
        :param pid:
        :return: time left in minutes
        """
        # This method will calculate the time left for the package.  To do this we find the difference between the
        # current time and the deadline time.

        package = self.all_packages.search(pid)
        truck_id = package.truck
        current_time = self.trucks[truck_id].current_time
        deadline = package.deadline
        time_left = (deadline.hour * 60 + deadline.minute) - (current_time.hour * 60 + current_time.minute)
        return time_left

    def calculate_distance(self, truck_location):
        for ids in range(1, 41):
            if self.all_packages.search(ids).status != "Delivered":
                self.all_packages.search(ids).distance = self.distance_table.search(truck_location).search(
                    self.all_packages.search(ids).delivery_location_id)

    def calculate_elapsed_time(self, next_package):
        """
        Method to calculate the elapsed time
        :param next_package: next package to deliver
        :return: elapsed time
        """
        distance = float(self.all_packages.search(next_package).distance)
        speed = float(18) / 60  # Speed of the truck
        elapsed_time = distance / speed
        return elapsed_time

    # Greedy Algorithm Approach
    def get_next_package(self, truck):
        """
        Method to get the next package for a truck to deliver using a greedy algorithm approach
        Prior to this method, the minute per mile(mpm) is calculated for each package
        The lower the mpm, the higher the priority
        The method sorts the packages by mpm in descending order
        The package with the lowest mpm is popped from the list and returned
        :param truck: truck id
        :return: next package id to deliver
        """
        next_package_list = self.trucks[truck].delivery_list  # Get the delivery list for the truck
        # Sort the package by minute per mile
        next_package_list.sort(key=lambda x: (self.all_packages.search(x).minute_per_mile, [1]), reverse=True)
        next_package = next_package_list.pop()  # Get the next package from the next_package_list
        return next_package  # Return the next package

    """ Methods to Update Package and Truck Attributes"""

    def update_package_attributes(self, truck):
        for package in self.trucks[truck].delivery_list:
            truck_location = self.trucks[truck].truck_location
            package_location = self.all_packages.search(package).delivery_location_id
            distance = self.get_distance(truck_location, package_location)
            self.all_packages.search(package).distance = distance
            self.all_packages.search(package).time_left = self.calculate_time_left(package)
            self.all_packages.search(package).minute_per_mile = self.calculate_minute_per_mile(package)

    def update_truck_current_time(self, truck, elapsed_time):
        """
        Method to update the truck's current time
        :param truck: truck id
        :param elapsed_time: elapsed time in minutes
        :return: None
        """
        old_time = self.trucks[truck].current_time  # Get the current time
        c_old_time = timedelta(hours=old_time.hour,
                               minutes=old_time.minute)  # Convert the current time to a timedelta object
        time_to_increase = timedelta(minutes=int(elapsed_time))  # Convert the elapsed time to a timedelta object
        current_time = c_old_time + time_to_increase  # Add the elapsed time to the current time
        new_time = current_time.total_seconds() / 60
        self.trucks[truck].current_time = time(int(new_time // 60), int(new_time % 60))

    def update_truck_mileage(self, truck, distance_traveled: float):
        """
        Method to update the truck's mileage
        :param truck: truck id
        :param distance_traveled: distance traveled
        :return: None
        """
        truck_mileage = self.trucks[truck].truck_mileage
        truck_mileage += float(distance_traveled)
        self.trucks[truck].truck_mileage = truck_mileage

    def update_truck_location(self):
        pass

    """Procedure to Deliver the Packages"""

    def drive_to_location(self, truck, next_package):
        """Before leaving we set the destination, calculate the distance, and time to travel"""
        destination = self.all_packages.search(next_package).delivery_location_id
        distance_to_travel = self.all_packages.search(next_package).distance  # Get the distance to travel
        t = self.calculate_elapsed_time(next_package)  # Calculate the elapsed time
        # Convert t to a time object
        elapsed_time = timedelta(minutes=int(t)).total_seconds() / 60

        """Now we travel to the location"""
        self.update_truck_current_time(truck, elapsed_time)  # Update the truck's current time
        self.update_truck_mileage(truck, distance_to_travel)  # Update the truck's mileage
        self.trucks[truck].truck_location = destination  # Update the truck's location

    def truck_return_to_hub(self, truck):
        destination = 0
        distance_to_travel = float(self.get_distance(self.trucks[truck].truck_location, destination))
        speed = float(18) / 60  # Speed of the truck
        elapsed_time = distance_to_travel / speed
        self.update_truck_current_time(truck, elapsed_time)
        self.update_truck_mileage(truck, distance_to_travel)
        self.trucks[truck].truck_location = destination
        self.trucks[truck].return_time = self.trucks[truck].current_time
        self.trucks[truck].truck_status = False

    def package_delivery(self, next_package, truck):
        """Now we deliver the package"""
        self.all_packages.search(next_package).status = "Delivered"  # Update the package status
        self.all_packages.search(next_package).time_delivered = self.trucks[
            truck].current_time  # Set the time delivered
        self.all_packages.search(next_package).distance = 0  # Set the distance to 0
        self.all_packages.search(next_package).time_left = 0  # Set the time left to 0
        self.all_packages.search(next_package).minute_per_mile = 0  # Set the minute per mile to 0

    def deliver_next_package(self, truck):
        while len(self.trucks[truck].delivery_list) > 0:
            next_package = self.get_next_package(truck)  # Get the next package using the greedy algorithm approach
            self.drive_to_location(truck, next_package)  # Drive to the location
            self.package_delivery(next_package, truck)  # Deliver the package
            self.update_package_attributes(truck)  # Update the package's attributes

        if len(self.trucks[truck].delivery_list) == 0:
            self.truck_return_to_hub(truck)

    def delivery_truck_packages(self, truck):
        self.start_truck(truck)
        self.initialize_delivery_list(truck)
        self.deliver_next_package(truck)

    def start_truck(self, truck):
        self.trucks[truck].truck_status = True  # Start the truck
        self.trucks[truck].current_time = self.trucks[
            truck].departure_time  # Set the current time to the departure time

    def initialize_delivery_list(self, truck):
        for package in self.trucks[truck].delivery_list:  # Because we are delivering packages
            self.all_packages.search(package).status = "En Route"  # Update delivery list packages to En Route
            self.all_packages.search(package).time_en_route = self.trucks[truck].current_time  # Set time en route
            self.all_packages.search(package).distance = self.get_distance(self.trucks[truck].truck_location,
                                                                           # Set how far the package is from the truck
                                                                           self.all_packages.search(
                                                                               package).delivery_location_id)
            self.all_packages.search(package).time_left = self.calculate_time_left(package)  # Set the time left
            self.all_packages.search(package).minute_per_mile = self.calculate_minute_per_mile(
                package)  # Set the minute per mile

    def deliver_packages(self):
        self.delivery_truck_packages(1)
        self.trucks[3].departure_time = self.trucks[1].return_time
        self.delivery_truck_packages(2)
        self.delivery_truck_packages(3)

    def setup_delivery_environment(self):
        """
        Procedure to set up the delivery environment
        :return: None
        """
        self.populate_packages()
        self.populate_distance_table()
        self.populate_location_id_table()
        self.add_truck_label_to_packages()
        self.set_location_id()
        self.set_package_time_at_hub()
        self.set_initial_distances(0)
        self.set_time_en_route()
        self.set_deadline()
        self.load_packages()
