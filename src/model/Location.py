class Location:
    def __init__(self, location_id, address, zip_code, distance_list):
        self.location_id = location_id
        self.address = address
        self.zip_code = zip_code
        self.distance_list = distance_list

    # TODO - Determine needed methods for the Location class
    # Method to return a string representation of the Location object
    def __str__(self):
        return f"{self.location_id}, {self.address}, {self.zip_code}"
