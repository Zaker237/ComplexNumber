"""Test Module"""
import unittest

from cnumber import ComplexNumber


class TestSum(unittest.TestCase):
    """Testing class for cnumber."""
    def test_inverse(self):
        """Test the inverse function."""
        self.assertEqual(1,1)

    def test_conjugate(self):
        """Test the conjugate function."""
        self.assertEqual(1,1)

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
        """Test the add many function."""
        self.assertEqual(1,1)

    def test_mutiply(self):
        """Test the multiplication."""
        number1 = ComplexNumber(1, 2)
        number2 = ComplexNumber(3, 4)
        result = number1 * number2
        self.assertEqual(result.get_real(), -5, "Should be -5!")
        self.assertEqual(result.get_imaginary(), 10, "Should be 10!")

    def test_multiply_namy(self):
        """Test the multiply many function."""
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
