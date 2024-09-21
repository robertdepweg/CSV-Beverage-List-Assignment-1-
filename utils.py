# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""Utility module"""

class CSVprocessor:
    """Obtains data from csv file"""

    from beverage import Beverage

    def csv_importer(self, path_to_csv, bev_col):
        """Imports csv file to be written"""
        with open(path_to_csv, "r", encoding="utf-8") as infile:
            line = infile.readline().replace("\n", "")
            while line:
                self.data_reader(line, bev_col)

                line = infile.readline().replace("\n", "")
    
    def data_reader(self, line, bev_col):
        """Splits line up and adds it to beverage collection instance"""
        parts = line.split(',')
        
        bev = self.Beverage(parts[0], parts[1], parts[2], float(parts[3]), parts[4])

        bev_col.add(bev)