#  File:       file_io.py
#  Purpose:     Read information from a file on your computer,
#               and/or write that information to another file
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 02:30 PM

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("file_io.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
