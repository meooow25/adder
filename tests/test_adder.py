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

    def test_addmany(self):
        nums = [i for i in range(10 ** 3)]
        sum_ = sum(nums)
        self.assertEqual(sum_, adder_logic.add(*nums))

    def test_add2many(self):
        nums = [i for i in range(10 ** 7)]
        sum_ = sum(nums)
        self.assertEqual(sum_, adder_logic.add(*nums))

if __name__ == '__main__':
    unittest.main()
