#  File:       lucky_number.py
#  Purpose:    Example : While loop test
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 30th August 2016, 12:00 PM

import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print (num)

    if num == 5:
        print ("Sorry, you lose!")
        break
    count += 1
else:
    print ("You win!")
