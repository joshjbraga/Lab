# Joshua Braga
# Lab 12
# 11/18/2022



class Account:

    def __init__(self, name):
        self._account_name: str = f'{name}'
        self._account_balance: int = 0
    '''This function initializes the account'''

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            return False

    '''This function sees if your deposit is a real positive numer
        and if it is, that amount is added to the account'''

    def withdraw(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance -= amount
            return True
        else:
            return False
    '''This function sees if your withdrawal is a real positive numer
        and if it is, that amount is subtracted to the account'''

    def get_balance(self) -> str:
        return f'{self._account_balance}'
    '''This function grabs the amount left in the account'''

    def get_name(self) -> str:
        return f'{self._account_name}'
    '''This function grabs the name from the account'''