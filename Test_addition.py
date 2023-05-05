import unittest

def addition(num1, num2):
    """
    Calculate the sum of the two given integers
    """
    sum = num1 + num2
    return sum

class TestAddition(unittest.TestCase):
    """
    Test cases for the addition function
    """
    def test_positive(self):
        self.assertEqual(addition(2, 3), 5)
    
    def test_negative(self):
        self.assertEqual(addition(-2, -3), -5)
    
    def test_zero(self):
        self.assertEqual(addition(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
