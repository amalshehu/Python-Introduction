#!/usr/bin/python3

person = {'Name': 'Amal Shehu', 'Age': 23, 'Blood Group': 'A+'}
person['Name'] = input("Enter your name :")
person['Age'] = input("Enter your age :")  # update existing entry
person['Blood Group'] = input("Enter your Blood Group :")
person['Language'] = "Python"
c = input("Do you want to print the details ? (y/n)")

if (c == 'y'):
    print("############################################################")
    print ("Name :", person['Name'])
    print ("Age: ", person['Age'])
    print ("Blood Group :", person['Blood Group'])
    print ("person['Language']: ", person['Language'])

elif (c == 'n'):
    print ("Thank You! Have a nice day!!!")

else:
    print ("Invalid Input")
