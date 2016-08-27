# Program to convert km into miles

# take input from the user
km = float(input('How many km?: '))

# conversion factor
conv_fac = 0.6

# calculate miles
miles = km * conv_fac
print('%0.3f km is equal to %0.3f miles' %(km,miles))
