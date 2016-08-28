#  File:       loop_inside_loop.py
#  Purpose:    Example: how to use a loop inside a loop
#              a nested while loop

#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 08:05 PM


print ("Program Started")

x = 1
while (x < 6):
    print() # prints a new line
    print ("x = " + str(x)) #  printing of the next item
                            # to be on the same line
    x = x + 1
    y = 1
    while (y < 6):
        print ("y = " + str(y),) #  printing on the same line
        y = y + 1
        z = 1
        while (z < 6):
            print ("z = " + str(z),) #  printing on the same line
            z = z + 1
        print() # prints a new line
'''
See that with a loop repeating 5 times,
inside a loop that repeats 5 times
inside a loop that repeats 5 times
means that we can control 125 processes.
'''
