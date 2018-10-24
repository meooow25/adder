import argparse

import adder_logic

parser = argparse.ArgumentParser(description='Adds integers')
parser.add_argument('nums', type=int, nargs='+', help='Integer to add and multiply')
args = parser.parse_args()

sum_ = adder_logic.add(*args.nums)
product_ = adder_logic.mult(*args.nums)
print('The sum is {} and the product is {}'.format(sum_, product_))
