import unittest

def factorial(integer):
    """
    Calculate the factorial of a given integer
    """
    if integer < 0:
        raise ValueError("Error: Negative number.")
    if integer == 0:
        return 1
    else:
        return integer * factorial(integer-1)

class TestFactorial(unittest.TestCase):
    """
    Test cases for the factorial function
    """
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == '__main__':
    unittest.main()
