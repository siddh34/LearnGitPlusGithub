import unittest
import sys
sys.path.append('..')
from fun import add 

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        print("Testing addition of positive numbers")
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        print("Testing addition of negative numbers")
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_number(self):
        print("Testing addition of integers")
        self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()