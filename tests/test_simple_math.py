# tests/test_simple_math.py

import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(1, 2), 3)

    def test_soustraction(self):
        self.assertEqual(SimpleMath.soustraction(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
