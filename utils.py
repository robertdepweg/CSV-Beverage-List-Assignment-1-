# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""Obtains data from csv file"""

class CSVProcesser:
    """"""
    from beverage import BeverageCollection

    def csv_importer(self, ui, loaded_value=False):
        """"""
        
        try:
            infile = open('beverage_list.csv', 'r')
            line = infile.readline().replace("\n", "")

            for line in infile:
                line = line.split(',')
                bev.beverage_list.append(line)
            loaded_value = True
            return loaded_value

        except IOError:
            print('IOError: No file with that name.')
        except Exception as message:
            print(message)

        pass

