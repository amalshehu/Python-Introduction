#  File:       factorial_recursion.py
#  Purpose:    Example: FActorial using recursion
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 11:10 PM

num = int(input("Enter a number"))  # Convert to an int


def factorial(num):
    if (num == 0):
        return
    else:
        return num*factorial(num-1)  # Factorial using recursion

result = factorial(num)
print(result)
