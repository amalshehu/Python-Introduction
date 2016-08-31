#  File:       animals_class.py
#  Purpose:    Example : Implementation of class (OOP)
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 31st August 2016, 09:50 AM



class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("Deer",10)
hippo.description()
sloth = Animal("Rocky",15)
ocelot = Animal("Rick",11)
print hippo.health
print sloth.health
print ocelot.health
