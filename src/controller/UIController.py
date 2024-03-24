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

        #  Assign trucks and drivers
        delivery_manager.assign_driver_to_truck(1, 1, drivers, trucks)
        delivery_manager.assign_driver_to_truck(2, 2, drivers, trucks)
        trucks.print_all_values()
        # drivers.print_all_values()
        # delivery_manager.unassign_driver_from_truck(1, 1, drivers, trucks)

        # trucks.print_all_values()
        # drivers.print_all_values()

        print("Packages ATH to Deliver: " + str(delivery_manager.ath_packages_to_deliver(trucks)))
        # This while statement checks if there are any trucks that have packages to deliver.
        #
        while delivery_manager.ath_packages_to_deliver(trucks) > 0:
            print("You still have " + str(delivery_manager.ath_packages_to_deliver(trucks)) + " packages to deliver.")
            for truck in range(1, 4):
                num_packages = len(trucks.search(truck).delivery_list)
                print(trucks.search(truck).truck_status)
                if num_packages > 0 and trucks.search(truck).truck_status:
                    print("Truck " + str(truck) + " has " + str(num_packages) + " packages to deliver.")
                    print("Truck " + str(truck) + " is ready to depart.")
                elif num_packages > 0 and not trucks.search(truck).truck_status:
                    print("Truck " + str(truck) + " has " + str(num_packages) + " packages to deliver.")
                    print("Truck " + str(truck) + " is not ready to depart.")

                input("Hit any key to continue")
                pass

        # TODO - Address the fact that packages 6, 26, 29, 33 do not arrive until 9:05 AM. Thus, before 09:05AM it needs to show that the package is at the hub and that the arrival time is None.
        #  After 09:05AM, the package should show that it is in transit to the delivery location.

        # TODO - Address the fact that package 9 has the wrong address until 10:20 AM. The address should be corrected at 10:20 AM. Before 10:20 it should show the wrong address.
        #  After 10:20 AM it should show the correct address.
