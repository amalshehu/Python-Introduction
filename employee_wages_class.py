#  File:       inheritance_triangle.py
#  Purpose:    Inheritance is a tricky concept, so let's go through it step by step.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 11:29 AM

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00
