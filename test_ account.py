# Test Cases
import account

account = Account()
print(account.deposit(100))
print(account._account_balance)
print(account.deposit(0))
print(account._account_balance)
print(account.deposit(-100))
print(account._account_balance)

print(account.withdraw(10))
print(account._account_balance)
print(account.withdraw(0))
print(account._account_balance)
print(account.withdraw(-10))
print(account._account_balance)