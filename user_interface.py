# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""User interface module"""

class UserInterface:
    """Handles all menu interface and options"""

    BEVERAGE_LIST_MIN = '1'
    BEVERAGE_LIST_MAX = '5'

    def print_header(self):
        """Prints options for choosing, returns choice"""
        print("\nSelect an option from the menu:")
        print("1. Load File")
        print("2. Print List")
        print("3. Search List")
        print("4. Add New Beverage")
        print("5. Exit\n")
        user_choice = input("> ")
        print()
        self.check_choice_validity(user_choice)
        return user_choice

    def check_choice_validity(self, user_choice):
        """Checks if choice submited is numberic and is between 1 and 5 inclusively"""
        if user_choice.isnumeric() and self.BEVERAGE_LIST_MIN <= user_choice <= self.BEVERAGE_LIST_MAX:
            return True
        else:
            self.invalid_choice_message()

    def invalid_choice_message(self):
        """Displays invalid choice message into terminal"""
        print("That is not a valid choice.")
        print("Please select a valid integer from 1 to 5.")
        
    def processing_message(self):
        """Tells the user the CSV data is being processed"""
        print(f"Processing... \n")

    def csv_completion_message(self):
        """Informs user the csv data is loaded"""
        print("The CSV file is loaded and ready.")

    def csv_finished_message(self):
        """Tells user CSV file is already prepared"""
        print("The CSV file has already been loaded in!")

    def user_addition(self):
        """Prompts user to add their beverage's characteristics, then adds to bev instance"""
        id = input("Please type your beverage's id: ")
        name = input("Please type your beverage's name: ")
        pack = input("Please type your beverage's pack: ")
        price = input("Please type your beverage's price: ")
        active = input("Please type your beverage's avalability: ")
        return f"{id}, {name}, {pack}, {price}, {active}"

    def print_list(self, bev_col):
        """Prints beverage collection items"""
        print(bev_col)

    def search_prompt(self):
        """Prompts user to search for their chosen beverage"""
        print("Please type the name of the drink you want to search for:")
        search_term = input("> ")
        return search_term

    def print_file_not_found_error(self):
        """Prints file not found error"""
        print("The file is not found! Please check on its status.")
    
    def print_empty_file_error(self):
        """Prints empty file error"""
        print("The file is empty! Please check on its status.")
    
    def exit_message(self):
        """Prints message that the program is being exited"""
        print("Exiting...")
