import datetime
from datetime import time


class Truck:
    """
    Constructor for the Truck class
    """

    def __init__(self, truck_id, truck_driver, truck_location, truck_status, truck_mileage, delivery_list,
                 departure_time: datetime.time = None, current_time: datetime.time = None, speed=18.0):
        self.truck_id = truck_id  # Set in program
        self.truck_driver = truck_driver  # Set in program
        self.truck_location = truck_location  # Set in program
        self.truck_status = truck_status  # Set in program
        self.truck_mileage = truck_mileage  # TODO Add Method
        self.delivery_list = delivery_list  # Set in program
        self.departure_time = departure_time  # Set in program
        self.current_time = current_time  # TODO Add Method
        self.speed = speed  # Speed set in program

    # Method to calculate the mileage
    def update_mileage(self):
        # TODO - Implement method to calculate the mileage
        pass

    # Method to calculate the current time
    def update_current_time(self):
        # TODO - Implement method to calculate the current time
        pass

    def __str__(self):
        return (f"Truck ID: {self.truck_id}\n"
                f"Driver: {self.truck_driver}\n"
                f"Location: {self.truck_location}\n"
                f"Active: {self.truck_status}\n"
                f"Mileage: {self.truck_mileage}\n"
                f"Delivery List: {self.delivery_list}        Total Packages: {len(self.delivery_list)}\n"
                f"Departure Time: {self.departure_time}\n"
                f"Current Time: {self.current_time}\n"
                f"Speed: {self.speed} miles/minute\n"
                f"+-----------------------------------------+")
