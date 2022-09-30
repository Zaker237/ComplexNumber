"""Test Module"""
from cgitb import reset
import unittest

from cnumber import ComplexNumber


class TestSum(unittest.TestCase):
    """Testing class for cnumber."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_inverse(self):
        pass

    def test_conjugate(self):
        pass

    def test_sum(self):
        """Test the summe."""
        number1 = ComplexNumber(1, 2)
        number2 = ComplexNumber(3, 4)
        self.assertEqual(
            number1 + number2,
            ComplexNumber(4, 6),
            "Should be 4 + 6i"
        )

    def test_sum_namy(self):
        pass

    def test_multiply_namy(self):
        pass

    def test_mutiply(self):
        """Test the multiplication."""
        number1 = ComplexNumber(1, 2)
        number2 = ComplexNumber(3, 4)
        result = number1 * number2
        self.assertEqual(result.get_real(), -5, "Should be -5!")
        self.assertEqual(result.get_imaginary(), 10, "Should be 10!")

    def test_multiply_namy(self):
        pass


if __name__ == '__main__':
    unittest.main()
