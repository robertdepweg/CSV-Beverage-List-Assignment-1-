# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""Program code"""

def main(*args):
    """Method to run program"""
    
    # First party imports
    import os

    # Third party imports
    from user_interface import UserInterface
    from beverage import BeverageCollection

    BEVERAGE_LIST_MAX = 5

    user_choice = ''
    path_to_csv_file = "../cis226-inclass-1-robertdepweg/employees.csv"

    ui = UserInterface()
    bev = BeverageCollection()

    user_choice = ui.print_list()

    try:
        ui.check_user_validity(user_choice)
    except ValueError:


    # Exit
    os._exit


