#!/usr/bin/python3

person = {'Name': 'Amal Shehu', 'Age': 23, 'Blood Group': 'A+'}

person['Name'] = input("Enter your name :")

person['Age'] = input("Enter your age :")  # update existing entry
person['Blood Group'] = input("Enter your Blood Group :")
person['Language'] = "Python"


print ("############################################################")
print ("Name :", person['Name'])
print ("Age: ", person['Age'])
print ("Blood Group :", person['Blood Group'])
print ("person['Language']: ", person['Language'])
