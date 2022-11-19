# Test Cases
from account import ac
import unittest

class MyTestCase(unittest.TestCase):

    def test_deposit(self):
        self.assertEqual(ac.deposit(40, 40))