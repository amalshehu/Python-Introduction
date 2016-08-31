#  File:       shopping_cart.py
#  Purpose:    Inheritance is a tricky concept, so let's go through it step by step.
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 31st August 2016, 10:20 AM

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
