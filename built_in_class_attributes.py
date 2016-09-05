#!/usr/bin/python3

# __dict__: Dictionary containing the class's namespace.

# __doc__: Class documentation string or none, if undefined.

# __name__: Class name.

# __module__: Module name in which the class is defined. This attribute is
# "__main__" in interactive mode.

# __bases__: A possibly empty tuple containing the base classes, in the order
#   of their occurrence in the base class list.


class Engineer:
    'Common base class for all Engineers'
    engCount = 0

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
        Engineer.engCount += 1

    def displayCount(self):
        print ("Total Engineer %d" % Engineer.engCount)

    def displayEngineer(self):
        print ("Name : ", self.name,  ", wage: ", self.wage)

emp1 = Engineer("Tom", 20000)
emp2 = Engineer("Jerry", 50000)
print ("Engineer.__doc__:", Engineer.__doc__)
print ("Engineer.__name__:", Engineer.__name__)
print ("Engineer.__module__:", Engineer.__module__)
print ("Engineer.__bases__:", Engineer.__bases__)
print ("Engineer.__dict__:", Engineer.__dict__)
