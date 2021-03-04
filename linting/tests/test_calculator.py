from unittest import TestCase
from calculator import mul


class CalculatorTest(TestCase):
    def test_mul(self) -> None:
        self.assertEqual(mul(2, 2), 4)