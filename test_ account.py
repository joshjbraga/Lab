# Test Cases
from account import Account

def test__init__():
    testName = Account('Jeremy')
    assert testName.get_name() == 'Jeremy'
    assert testName.get_balance() == 0

def test_deposit():
    testName = Account('Jeremy')
    testName.deposit(-90)
    assert testName.get_balance() == 0
    testName.deposit(90)
    assert testName.get_balance() == 90
    testName.deposit(0)
    assert testName.get_balance() == 90

def test_withdrawl():
    testName = Account('Jeremy')
    testName.deposit(90)
    testName.withdraw(-80)
    assert testName.get_balance() == 0
    testName.deposit(80)
    assert testName.get_balance() == 10
    testName.deposit(0)
    assert testName.get_balance() == 10