class Package:
    """
    Class to represent all packages
    """

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, time_at_hub,
                 time_en_route, time_delivered, truck, delivery_location_id, time_left, distance_to_delivery,
                 minute_per_mile):
        """
        Constructor for the Packages
        :param package_id:
        :param address:
        :param city:
        :param state:
        :param zip_code:
        :param deadline: time the package needs to be delivered by
        :param weight:
        :param notes:
        :param status:
        :param time_at_hub:
        :param time_en_route:
        :param time_delivered:
        :param truck:
        :param delivery_location_id:
        :param time_left:
        :param distance_to_delivery:
        :param minute_per_mile:
        """
        self.package_id = package_id  # Set from CSV
        self.address = address  # Set from CSV
        self.city = city  # Set from CSV
        self.state = state  # Set from CSV
        self.zip_code = zip_code  # Set from CSV
        self.deadline = deadline  # Set from CSV
        self.weight = weight  # Set from CSV
        self.notes = notes  # Set from CSV
        self.status = status  # Set in program
        self.time_at_hub = time_at_hub  # Set in program
        self.time_en_route = time_en_route  # Set in program
        self.time_delivered = time_delivered  # Set in program
        self.truck = truck  # Set in program
        self.delivery_location_id = delivery_location_id  # Method stated
        self.time_left = time_left  # Method stated
        self.distance = distance_to_delivery  # Method stated
        self.minute_per_mile = minute_per_mile  # Method stated

    # def __str__(self):
    #     """
    #     Method to return a string representation of the Packages object
    #     :return: string representation of the Packages object
    #     """
    #     return (
    #         f"+-----------------------------------------+\n"
    #         f"| Package ID: {self.package_id}\n"
    #         f"| Delivery Location ID: {self.delivery_location_id}\n"
    #         f"| Address: {self.address}  {self.city}, {self.state} {self.zip_code}\n"
    #         f"| Weight: {self.weight}\n"
    #         f"| Notes: {self.notes}\n|\n"
    #
    #         f"| Status: {self.status}\n|\n"
    #                     f"| Time at Hub: {self.time_at_hub}   Time En Route: {self.time_en_route}       Time Delivered: {self.time_delivered}\n|\n"
    #         f"| Deadline: {self.deadline}       Time Left: {self.time_left}       Dist. to Delivery: {self.distance}\n"
    #
    #         f"| Assigned Truck: {self.truck}\n"
    #         f"| Min/Mile: {self.minute_per_mile}\n"
    #         f"+-----------------------------------------+\n"
    #     )

    def __str__(self):
        """
        Method to return a string representation of the Packages object
        :return: string representation of the Packages object
        """
        return (
            f"{self.package_id:2} | "
            f"{self.address[:35]:35} |{self.city[:15]:15} |{self.zip_code:8} | "
            f"{self.weight:7} | "
            f"{self.status:10} | "
            f"{self.time_delivered:} | "
            f"{self.deadline:} | "
            f"{self.truck:2} | "
        )

    def set_delivery_location_id(self):
        # TODO - Implement method: set_delivery_location_id
        """
        This method sets the delivery location id for all the packages.
        :return: delivery location id
        """
        # To set the delivery_location_id for the package, it will need to take the address and zip code and
        # format it in away. We can use this to reference a hashtable that we will create later and it will
        # retrieve the location ID from that.
        pass

    def calculate_distance(self, current_location_id):
        # TODO - Implement method: calculate_distance
        """
        Method to calculate the distance
        :param current_location_id:
        :return: distance
        """
        # This method will calculate the distance for the package.  To do this we will need to take the
        # current location id and the delivery location id and calculate the distance between the two.
        # We will need to use the distance matrix to do this.
        pass

    def calculate_time_left(self, current_time, deadline_time):
        # TODO - Implement method: calculate_time_left
        """
        Method to calculate the time left
        :param current_time:
        :param deadline_time:
        :return: time left
        """
        # This method will calculate the time left for the package.  To do this we find the difference between the
        # current time and the deadline time.
        pass

    def set_mpm(self, time, distance):
        # TODO - Implement method: set_mpm
        """
        Method to calculate the minute per mile
        :param  time:
        :param  distance:
        :return: minute per mile
        """
        # This method will calculate the minute per mile for the package.  To do this we will need to take the
        # time and distance and divide them to get the minute per mile.
        pass
