from src.model.NewDeliveryManager import NewDeliveryManager
from datetime import datetime


class UIController:
    def __init__(self):
        """
        Constructor for the UIController
        :return: None
        """

    @staticmethod
    def option_1():
        """
        Method for handling option 1
        :return: None
        """
        dm = NewDeliveryManager()
        dm.setup_delivery_environment()
        dm.deliver_packages()

        # Let's print the total distance traveled by all trucks
        t1_miles = dm.trucks[1].truck_mileage
        t2_miles = dm.trucks[2].truck_mileage
        t3_miles = dm.trucks[3].truck_mileage
        total_miles = t1_miles + t2_miles + t3_miles
        input("\n\n\nDelivering all packages. Press Enter to continue...")
        input("\nDeliveries Complete.")
        input(f"\nTotal miles traveled by all trucks: {total_miles}")
        input("\n\n\nPress Enter to view all packages...")
        print(f"{' ' * 92}Time")
        print(f"ID | Address{' ' * 29}| "f"City{' ' * 11}|Zip Code | Weight  |Status      |Delivered |Deadline  |Truck")
        print(
            "---|-------------------------------------|----------------|---------|---------|------------|----------|----------|-----")

        dm.all_packages.print_all_values()
        input("\nPress Enter to return to the menu.\n")

    @staticmethod
    def option_2():
        """
        Method for handling option 2
        :return:
        """
        dm = NewDeliveryManager()
        dm.setup_delivery_environment()
        userinput_id = int(input("Enter the package ID: "))
        print(type(userinput_id))
        print(dm.all_packages.search(userinput_id).package_id, dm.all_packages.search(userinput_id).address,
              dm.all_packages.search(userinput_id).city, dm.all_packages.search(userinput_id).zip_code,
              dm.all_packages.search(userinput_id).weight, dm.all_packages.search(userinput_id).status,
              dm.all_packages.search(userinput_id).time_delivered, dm.all_packages.search(userinput_id).deadline,
              dm.all_packages.search(userinput_id).truck)

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
