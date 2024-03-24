class Driver:
    """
    Class to represent a driver
    """

    def __init__(self, driver_id, status_active, assigned_truck):
        """
        Constructor for the Driver class
        :param driver_id:
        :param status_active:
        :param assigned_truck:
        """
        self.driver_id = driver_id  # Set in program
        self.status_active = status_active  # Set in program
        self.assigned_truck = assigned_truck  # Set in program

    def __str__(self):
        """
        Method to return a string representation of the Driver object
        :return: string representation of the Driver object
        """
        return f"Driver: {self.driver_id}, {self.status_active}, {self.assigned_truck}"
