#  File:       is_even.py
#  Purpose:    To check a number is an integer or not
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 05:50 PM


x = raw_input("Enter a number :")


def is_int(x):
                       # if x - int(x) > 0: #failed
        if x % 1 == 0:
            return True
        else:
            return False
