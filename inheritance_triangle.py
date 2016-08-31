#  File:       inheritance_triangle.py
#  Purpose:    Inheritance is a tricky concept, so let's go through it step by step.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 31st August 2016, 10:29 AM

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Added inherited Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
