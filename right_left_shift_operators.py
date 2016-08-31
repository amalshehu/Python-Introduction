#  File:       right_left_shift_operators.py
#  Purpose:     Use the left shift (<<) and right shift (>>) operators to slide masks into place.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Wednesday 31st August 2016, 04:40 PM

def flip_bit(number, n):
    mask = (0b1 << n-1)
    slip = number ^ mask
    result = bin(slip)
    return result
print flip_bit(0b111, 2)
