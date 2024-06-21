# tests/test_simple_math.py

import unittest
from src.simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(1, 2), 3)

    def test_soustraction(self):
        self.assertEqual(SimpleMath.soustraction(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
