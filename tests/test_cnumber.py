"""Test Module"""
import unittest

from cnumber import ComplexNumber


class TestSum(unittest.TestCase):
    """Testing class for cnumber."""
    def test_sum(self):
        """Test the summe."""
        number1 = ComplexNumber(1, 2)
        number2 = ComplexNumber(3, 4)
        self.assertEqual(
            number1 + number2,
            ComplexNumber(4, 6),
            "Should be 4 + 6i"
        )

    def test_mutiply(self):
        """Test the multiplication."""
        number1 = ComplexNumber(1 ,2)
        number2 = ComplexNumber(3, 4)
        self.assertEqual(
            number1 * number2,
            ComplexNumber(-5,10),
            "Should be 6!"
        )


if __name__ == '__main__':
    unittest.main()
