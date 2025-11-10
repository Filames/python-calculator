import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3, 2), -1)
    
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(3, 2), -1)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_div2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(13, 3), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()