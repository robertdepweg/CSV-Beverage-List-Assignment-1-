# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""User interface module"""

class UserInterface:
    """Handles all menu interface and options"""

    def print_header(self, user_choice):
        """Prints options for choosing, returns choice"""
        print("Select an option from the menu:")
        print("1. Load File")
        print("2. Print List")
        print("3. Search List")
        print("4. Add New Beverage")
        print("5. Exit")
        user_choice = input()
        return user_choice

    def check_user_validity(self, user_choice):
        try:
            while user_choice != "5":
                # Load File
                if user_choice == "1":
                    bev.            
                # Print List
                elif user_choice = "2":
                    
                # Search List
                elif user_choice == "3":

                # Add new beverage
                else:
                    bev.add()



        except ValueError:
            
        except :

    def get_beverage_list():
        """  """
        pass

    def print_list():
        """  """
        pass
