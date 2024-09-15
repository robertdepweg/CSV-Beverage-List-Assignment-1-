# Author:
# Class:
# Date:
#mostly csv processer
class CSVProcesser:
    """  """
    from beverage import BeverageCollection

    def file_loader():
        """  """
        
        try:
            infile = open('beverage_list.csv', 'r')
            infile.readline()

            for line in infile:
                line_values = ()
                line_values.append = line.split(',')


        except IOError:
            print('IOError: No file with that name.')
        except Exception as message:
            print(message)

        pass