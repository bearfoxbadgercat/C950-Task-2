from src.controller.UIController import UIController

# Create an instance of the UIController
controller = UIController()


# Method for loading the welcome message
def load_welcome_message():
    """
    Load the welcome message
    :return: None
    """
    print("Welcome to WGUPS!\n")


# Method for loading the menu
def load_menu():
    """
    Load the menu
    :return: The user's choice
    """
    print("Menu Options:")
    print("1. Deliver All Packages")
    print("2. Look Up Package at Specific Time")
    print("3. Exit Program")

    while True:
        choice = input("\nEnter your choice: ")
        if choice in ("1", "2", "3"):
            return choice
        else:
            print("Invalid choice. Please select a valid option.")


# Method for processing the user's choice
def process_choice(choice):
    """
    Process the user's choice
    :param choice: The user's choice
    :return: None
    """
    # Call the appropriate method in the controller based on the user's choice
    if choice == "1":
        controller.option_1()
    elif choice == "2":
        controller.option_2()
    elif choice == "3":
        controller.exit_program()

    else:
        print("Invalid choice. Please select a1 valid option.")


# Method for running the user interface
def run_ui():
    """
    Run the user interface
    :return: None
    """
    load_welcome_message()

    while True:
        choice = load_menu()
        process_choice(choice)


# Run the user interface
if __name__ == "__main__":
    """
    Run the user interface
    :return: None
    """
    run_ui()
