#!/usr/bin/python3

person = {'Name': 'Amal Shehu', 'Age': 23, 'Blood Group': 'A+'}

person['Name'] = input("Enter your name :")

person['Age'] = input("Enter your age :")  # update existing entry
person['Blood Group'] = input("Enter your Blood Group :")
person['Language'] = "Python"  # Add new entry

print ("Name :", person['Name'])
print ("person['Age']: ", person['Age'])
print ("person['Language']: ", person['Language'])
