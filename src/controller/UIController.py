from src.model.ChainingHashtable import ChainingHashTable
from src.model.DeliveryManager import DeliveryManager


class UIController:
    def __init__(self):
        """
        Constructor for the UIController
        :return: None
        """
        pass

    @staticmethod
    def option_1():
        """
        Method for handling option 1
        :return: None
        """
        print("Option 1 selected")
        # TODO Add code to handle option 1
        pass

    # write remaining options through 5
    @staticmethod
    def option_2():
        """
        Method for handling option 2
        :return:
        """
        print("Option 2 selected")
        # Hit any key to continue
        input("Hit any key to continue")
        # TODO Add code to handle option 2
        pass

    @staticmethod
    def option_3():
        """
        Method for handling option 3
        :return:
        """
        print("Option 3 selected")
        # TODO Add code to handle option 3
        pass

    @staticmethod
    def exit_program():
        """
        Method for exiting the program
        :return: None
        """
        confirmation = input("Are you sure you want to exit? (y/n): ")
        if confirmation.lower() == "y":
            print("Exiting program")
            # Add any cleanup code or additional actions needed before exiting
            exit()
        else:
            print("Returning to the menu.")

    @staticmethod
    def option_5():
        """
        This is only for testing purposes
        :return: None
        """

        # Initiate the Delivery Manager
        delivery_manager = DeliveryManager()

        # Step 1: Create WGUPS Environment

        # Declare empty hash tables using the ChainingHashTable class
        drivers = ChainingHashTable(2)  # Drivers
        trucks = ChainingHashTable(3)  # Trucks
        all_packages = ChainingHashTable(40)  # Packages
        distance_table = ChainingHashTable(27)  # Location Table
        location_id = ChainingHashTable(27)  # Location ID

        # Set up the WGUPS environment
        delivery_manager.setup_environment(drivers, trucks, all_packages, distance_table, location_id, distance_table)

        # all_packages.print_all_values()
        # location_table.print_all_values()
        # location_id.get_all()
        # print(all_packages.search(30))
        delivery_manager.assign_driver_to_truck(1, 1, drivers, trucks)
        delivery_manager.assign_driver_to_truck(2, 2, drivers, trucks)
        trucks.print_all_values()
        drivers.print_all_values()
        delivery_manager.unassign_driver_from_truck(1, 1, drivers, trucks)

        trucks.print_all_values()
        drivers.print_all_values()

        # Loop continues as long as there are packages left to deliver
        while delivery_manager.ath_packages_to_deliver(trucks) > 0:
            # Inform the user of the total number of packages still to be delivered
            print("You still have " + str(delivery_manager.ath_packages_to_deliver(trucks)) + " packages to deliver.")

            # Iterate through each truck by their ID (assumed range 1 to 3)
            for truck in range(1, 4):
                # Get the number of packages currently assigned to the truck
                num_packages = len(trucks.search(truck).delivery_list)
                # Print the current status of the truck (ready or not ready)
                print(trucks.search(truck).truck_status)

                # If the truck has packages and is marked as ready
                if num_packages > 0 and trucks.search(truck).truck_status:
                    # Inform the user of the number of packages to deliver and truck readiness
                    print("Truck " + str(truck) + " has " + str(num_packages) + " packages to deliver.")
                    print("Truck " + str(truck) + " is ready to depart.")
                # If the truck has packages but is not marked as ready
                elif num_packages > 0 and not trucks.search(truck).truck_status:
                    # Inform the user of the number of packages to deliver and truck's unavailability
                    print("Truck " + str(truck) + " has " + str(num_packages) + " packages to deliver.")
                    print("Truck " + str(truck) + " is not ready to depart.")

                # Wait for the user input to continue, ensuring they have time to read the status
                input("Hit any key to continue")
