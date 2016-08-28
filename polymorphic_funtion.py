#  File:       polymorphic_function.py
#  Purpose:    Example: polymorphic_function
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 08:28 PM


def twice(x):
    return (2 * x)

y = 5
print (twice(y))
z = "Spam "
print (twice(z))  # * operator is overloaded
print ("An example for polymorphism.The * opearator is overloaded.")
