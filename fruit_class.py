#  File:       Fruit_class.py
#  Purpose:    Example : Implementation of class (OOP)
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 30th August 2016, 10:15 PM

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
