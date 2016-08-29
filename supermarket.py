#  File:       supermarket.py
#  Purpose:    Example: Python dictionary
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Monday 29th August 2016, 11:35 AM

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])
