# Joshua Braga
# Lab 12
# 11/18/2022

class Account:

    def __init__(self):
        self._account_name = 0
        self._account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            return False

