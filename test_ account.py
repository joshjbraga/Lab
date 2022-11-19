# Test Cases
import account
import unittest

class MyTestCase(unittest.TestCase):

    def test_deposit(self):
        self.assertEqual(account.deposit(40, 40))
        self.assertEqual(account.deposit(0, 0))
        self.assertEqual(account.deposit(-40, 0))