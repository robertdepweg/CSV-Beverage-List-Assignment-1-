# Author: Robert Depweg
# Class: CIS226
# Date: 9/18/24
"""Beverage module"""

class Beverage:
    """Instance of single beverage"""

    def __init__(self, id, name, pack, price, active=False):
        """Constructor"""
        self.id = id
        self.name = name
        self.pack = pack
        self.price = price
        self.active = active

    def __str__(self):
        """Returns string of beverage"""
        return f"ID: {self.id}, Name: {self.name}, Pack: {self.pack}, Price: ${self.price}, Active Status: {self.active}"

class BeverageCollection:
    """Instance of a collection of beverages"""

    __beverage = []

    def add(self, addition):
        """Adds beverage to list"""
        # Used for both initially adding in through csv and by user
        self.__beverage.append(addition)

    def search(self, search_term):
        """Searches beverage list for user's input"""
        counter = 0
        for items in self.__beverage:
            if search_term in self.__beverage:    
                return f"{items[counter]}"
            else:
                counter += 1

    def __str__(self):
        """Returns string of beverage collection"""
        for items in self.__beverage:
            return f"{items}"