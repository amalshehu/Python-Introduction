#  File:       file_io.py
#  Purpose:     Read information from a file on your computer,
#               and/or write that information to file
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 03:00 PM

import os
print ("== if the file doesn't exist, create one ==")
if os.path.exists('text.txt'):
    print ("File exists")
else:
    print ("Creating the text.txt-file")
    my_file = open("text.txt", 'w')
    my_file.write("I'm the first line of the file!" +"\n")
    my_file.write("I'm the second line."+"\n")
    my_file.write("Third line here, boss."+"\n")
    my_file.close()

my_file = open("text.txt","r")
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()
