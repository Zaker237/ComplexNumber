from ComplexNumber import ComplexNumber
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        a = ComplexNumber(1,2)
        b = ComplexNumber(3,4)
        self.assertEqual(a+b, ComplexNumber(4,6), "Should be 4 +6i")

    def test_mutiply(self):
        a = ComplexNumber(1,2)
        b = ComplexNumber(3,4)
        self.assertEqual(a*b, ComplexNumber(-5,10), "Should be 6")

if __name__ == '__main__':
    unittest.main()
