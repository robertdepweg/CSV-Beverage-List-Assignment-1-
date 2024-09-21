# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""Program code"""

def main(*args):
    """Method to run program"""
    
    # First party imports
    import os

    # Third party imports
    import beverage 
    from user_interface import UserInterface
    from utils import CSVprocessor

    # Instances
    ui = UserInterface()
    bev_col = beverage.BeverageCollection()
    processor = CSVprocessor()

    # Flag to check if csv is written in or not
    csv_flag = False

    # Obtains user choice
    user_choice = ui.print_header()
    
    path_to_csv = "../cis226-assignment-1-robertdepweg/datafiles/beverage_list.csv"

    while user_choice != ui.BEVERAGE_LIST_MAX:
        if user_choice == '1':
            # Checks if file isn't already loaded
            if csv_flag != True:
                # Loads File
                try:
                    ui.processing_message()
                    processor.csv_importer(path_to_csv, bev_col) 
                    ui.csv_completion_message()
                    csv_flag = True
                except EOFError:
                    ui.print_empty_file_error()
                except FileNotFoundError:
                    ui.print_file_not_found_error()
            else:
                # If file is already loaded
                ui.csv_finished_message()
        # Prints List
        elif user_choice == '2' and csv_flag == True:
            ui.print_list(bev_col)    
        # Searchs List
        elif user_choice == '3' and csv_flag == True:
            search_term = ui.search_prompt()
            bev_col.search(search_term)
        # Adds new beverage to list
        elif user_choice == '4' and csv_flag == True:
            user_addition = ui.user_addition()
            bev_col.add(user_addition)

        # Prompts user again
        user_choice = ui.print_header()
        
    # Exit
    ui.exit_message()
    os._exit





