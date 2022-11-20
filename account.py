# Joshua Braga
# Lab 12
# 11/18/2022



class Account:
    '''
    This class is made to create and run an
    account that you can deposit and withdraw
    from.
    '''

    def __init__(self, name: str) -> None:
        '''
        This function initializes the account
        '''
        self.__account_name: str = f'{name}'
        self.__account_balance: float = 0


    def deposit(self, amount: float) -> bool:
        '''
        This function sees if your deposit is a real positive numer
        and if it is, that amount is added to the account
        '''
        if amount > 0:
            self.__account_balance += amount
            print(f'Account balance = {self.__account_balance}')
            return True
        else:
            return False


    def withdraw(self, amount: float) -> bool:
        '''
        This function sees if your withdrawal is a real positive numer
        and if it is, that amount is subtracted to the account
        '''
        if amount > 0:
            self.__account_balance = self.__account_balance - amount
            print(f'Account balance = {self.__account_balance}')
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        This function grabs the amount left in the account
        '''
        balance = self.__account_balance
        return balance

    def get_name(self) -> str:
        '''
        This function grabs the name from the account
        '''
        return f'{self.__account_name}'
