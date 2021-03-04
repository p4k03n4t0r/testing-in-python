from unittest import TestCase
from calculator import mul


class CalculatorTest(TestCase):
    def test_mul(self) -> None:
        result = mul(2, 3)
        self.assertEqual(result, 6)