#  File:       use_of_function.py
#  Purpose:    Example: FActorial using recursion
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 11:10 PM


factorial=1
num=input("Enter a number")
def factorial(n):
    if (n==0):
        return 1
    else:
        return factorial*factorial(n-1)
