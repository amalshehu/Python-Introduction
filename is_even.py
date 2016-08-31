#  File:       is_even.py
#  Purpose:    To check a number is even or not
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 05:50 PM

x = int(input("Enter a number :"))


def is_even(x):

    if x % 2 == 0:
        return True
    else:
        return False
