#  File:       digit_sum.py
#  Purpose:    To find the sum of digits.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 06:20 PM

x = int(input("Enter a number :"))


def digit_sum(x):
    total = 0
    digits = str(x)
    for item in digits:
        total = total + int(item)
    return total

print (digit_sum(x))
