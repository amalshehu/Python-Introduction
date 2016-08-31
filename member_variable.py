#  File:       member_variable.py
#  Purpose:    Referring to member variables
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 01:30 PM



class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car(model = "DeLorean", color = "silver", mpg = 88)
print my_car.model
print my_car.color
print my_car.mpg
