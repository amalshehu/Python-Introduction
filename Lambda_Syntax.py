#  File:       Lambda_Syntax.py
#  Purpose:    Example : Functional Programming
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 30th August 2016, 08:55 PM

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
print("Lambdas are useful when you need a quick function to do some work for you")
