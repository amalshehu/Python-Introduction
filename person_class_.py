#  File:       person_class.py
#  Purpose:    Example : Implementation of class (OOP)
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Tuesday 30th August 2016, 10:55 PM

import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person("Amal","Shehu", datetime.date(1993, 7, 16),
    "No. 12 Spike Street,Trivandrum","828 182 0382",
    "amalshehu@gmail.com")

print(person.name)
print(person.email)
print(person.age())
