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
        return (
            f"Driver Information Card\n"
            f"------------------------\n"
            f"Driver ID: {self.driver_id}\n"
            f"Status: {'Active' if self.status_active else 'Inactive'}\n"
            f"Assigned Truck: {self.assigned_truck}\n"
        )
