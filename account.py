# Joshua Braga
# Lab 12
# 11/18/2022

class Account:

    def __init__(self):
        self._account_name: str = '0'
        self._account_balance: int = 0

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> str:
        return f'{self._account_balance}'

    def get_name(self) -> str:
        return f'{self._account_name}'
