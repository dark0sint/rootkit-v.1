# test_main.py

import unittest
from io import StringIO
import sys
from main import main

class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Redirect stdout to capture print statements
        output = StringIO()
        sys.stdout = output
        
        # Simulate user input
        user_input = 'Alice\n'
        sys.stdin = StringIO(user_input)
        
        main()
        
        # Check the output
        self.assertIn("Hello, Alice! Welcome to the Rootkit application.", output.getvalue())
        
        # Reset stdout and stdin
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

if __name__ == '__main__':
    unittest.main()
