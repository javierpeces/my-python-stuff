#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# A fantastic tutorial here: 
# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
# This code (and the blog's one) is based on the contents of that page.
# Sample 'bad-bank' account management. No commissions, even in case of (unsupported) negative balance.
#

class Customer(object):
    """ 
        A customer with his account. The properties:
        - custid: Unique identifier, e. g. passport or driving license no. Fight fraud!!! ;-)
        - custname: Name.
        - balance: A float showing the money.
    """

    def __init__(self, custid, custname):
        """ Returns a customer object """ 
        self.custid = custid 
        self.custname = custname
        self.balance = 0.0

    def set_initial_balance(self, balance=0.0):
        """ Put money when creating the customer """
        self.balance = balance
        print("initial balance: %d" % self.balance) 

    def money_withdraw(self, amount):
        """ Returns the available after withdraw """
        if amount > self.balance:
            raise RuntimeError('Amount greater than the available one.')
        self.balance -= amount
        print("withdraw: %d" % amount)
        print("current balance: %d" % self.balance)
        return self.balance

    def money_deposit(self, amount):
        """ Returns the available after deposit """
        self.balance += amount
        print("deposit: %d" % amount)
        print("current balance: %d" % self.balance)
        return self.balance

"""
    And now, the first customer...
"""


if __name__ == "__main__":
    firstcustomer = Customer("12345678A", "Juan Español")
    firstcustomer.set_initial_balance( 1000.00 )
    print(firstcustomer.money_withdraw( 300.00 ))
    print(firstcustomer.money_deposit( 555.50 ))
    print(firstcustomer.money_withdraw( 9999.00 ))
    
    
# The last withdraw intentionally raises an error
#    $ ./50-five-min-a-day-objects.py
#    initial balance: 1000
#    withdraw: 300
#    current balance: 700
#    700.0
#    deposit: 555
#    current balance: 1255
#    1255.5
#    Traceback (most recent call last):
#      File "./bancomalo.py", line 43, in <module>
#        print(primercliente.sacar_pasta( 9999.00 ))
#      File "./50-five-min-a-day-objects.py", line 25, in money_withdraw
#        raise RuntimeError('Amount greater than the available one.')
#    RuntimeError: Amount greater than the available one.
