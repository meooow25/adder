import argparse

import adder_logic

parser = argparse.ArgumentParser(description='Adds integers')
parser.add_argument('nums', type=int, nargs='+', help='Integer to add')
args = parser.parse_args()

sum_ = adder_logic.add(*args.nums)
print('The sum is {}'.format(sum_))
