# test_utils.py

import unittest
from utils import greet_user

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Bob"), "Hello, Bob! Welcome to the Rootkit application.")

if __name__ == '__main__':
    unittest.main()
