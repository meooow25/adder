import unittest

from adder import adder_logic

class AdderTest(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(5, adder_logic.add(5))

    def test_add2(self):
        self.assertEqual(10, adder_logic.add(2, 8))

    def test_add3(self):
        self.assertEqual(102, adder_logic.add(2, 60, 40))

    def test_add2neg(self):
        self.assertEqual(-2, adder_logic.add(1, -3))

if __name__ == '__main__':
    unittest.main()
