import unittest
from part2.task2 import task2


class TestFractions(unittest.TestCase):
    def test_01(self):
        test_01 = task2.Rational(2, 4)
        self.assertEqual(test_01.fractional_format(), "1/2")
        self.assertEqual(test_01.floating_point_format(), "0.5")

    def test_02(self):
        test_02 = task2.Rational(8, 10)
        self.assertEqual(test_02.fractional_format(), "4/5")
        self.assertEqual(test_02.floating_point_format(), "0.8")

    def test_03(self):
        test_03 = task2.Rational(15, 6)
        self.assertEqual(test_03.fractional_format(), "5/2")
        self.assertEqual(test_03.floating_point_format(), "2.5")

    def test_04(self):
        test_04 = task2.Rational(63, 189)
        self.assertEqual(test_04.fractional_format(), "1/3")
        self.assertEqual(test_04.floating_point_format(), "0.33")

    def test_05(self):
        test_05 = task2.Rational(22, 13)
        self.assertEqual(test_05.fractional_format(), "22/13")
        self.assertEqual(test_05.floating_point_format(), "1.7")


if __name__ == "__main__":
    unittest.main()