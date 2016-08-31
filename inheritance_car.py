#  File:       inheritance_car.py
#  Purpose:    Methods from  parent classes
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 02:10 PM

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color,self.model,self.mpg)

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        Car.__init__(self,model,color,mpg)
        self.battery_type = battery_type


my_car = ElectricCar("Ferrari", "Red", "300", "molten salt")
print my_car.display_car()
