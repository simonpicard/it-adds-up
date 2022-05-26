import unittest
from math import *

from main import compteEstBon


class TestCEB(unittest.TestCase):
    def setUp(self):
        self.listTest = []
        self.listTest.append(
            (10, [1, 1, 1, 1, 1, 1], 1)
        )  # compte approchant 9
        self.listTest.append(
            (888, [100, 2, 75, 3, 1, 10], 0)
        )  # compte est bon
        self.listTest.append((837, [25, 50, 75, 3, 9, 5], 0))  # compte est bon
        self.listTest.append((444, [4, 4, 8, 8, 7, 5], 0))  # compte est bon
        self.listTest.append(
            (444, [5, 5, 5, 5, 5, 5], 6)
        )  # compte approchant 450
        self.listTest.append(
            (777, [8, 8, 8, 8, 8, 8], 9)
        )  # compte approchant 768
        self.listTest.append(
            (777, [8, 8, 8, 8, 9, 9], 1)
        )  # compte approchant 776

    def aTest(self, res, values, difference):
        t = fabs(compteEstBon(res, values).getMax() - res)
        self.assertEqual(t, difference)

    def test_CEB(self):
        for t in self.listTest:
            self.aTest(t[0], t[1], t[2])


if __name__ == "__main__":
    unittest.main()
