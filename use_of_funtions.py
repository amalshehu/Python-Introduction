#  File:       use_of_function.py
#  Purpose:    Example: use of a function
#  Programmer: Amal Shehu
#  Course:     Practice
#  Date:       Sunday 28th August 2016, 08:55 PM

'''


    This is a muliti-line comment (')
    Functions can be defined anywhere.But note that
    to define before calling it.

    We are using a  simple pause function,
    to pause a program until a key is pressed.

    When function called, all the lines in the
    function definition (def) are executed in order,
    then the program resumes at the point after the function call.

    This program script starts executing at the line:
    startMsg()
    followed by the line:
    clrScreen()
    followed by the line:
    print ("Testing me")


'''



def pause():
    input("\n\nPress any key to continue...\n\n")

def quitMessage():
    print ("Thanks for using this me")
    print ("Have a nice day!!!Goodbye")

def printThreeLines():
    for i in range(1,4):
        print ('Im from ' + str(i))

def printNineLines():
    for i in range(1,4):
        printThreeLines()

def startMsg():
    print ("Im demonstrating the use of Python functions")
    pause()

def blank_Line():
    print()

def clrScreen():
    for i in range(1,26):
        blank_Line()



startMsg()
clrScreen()
print ("Testing me")
printNineLines()
pause()
clrScreen()
printNineLines()
blank_Line()
printNineLines()
pause()
clrScreen()
quitMessage()
