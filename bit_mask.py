#  File:       bit_mask.py
#  Purpose:    A bit mask is just a variable that aids you with bitwise operations.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 04:30 PM

def check_bit4(input):
    mask=0b1000
    cresult=input & mask
    if cresult > 0 :
        return "on"
    else:
        return "off"
