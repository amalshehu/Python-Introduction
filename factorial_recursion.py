#  File:       use_of_function.py
#  Purpose:    Example: FActorial using recursion
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 11:10 PM



int num=  input ("Enter a number")
def factorial(num):
    if (num==0):
        return 1
    else:
        return num*factorial(num-1)

result=factorial(num)
print(result)
