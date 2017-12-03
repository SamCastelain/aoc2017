#!/usr/bin/env python3.6
import argparse

class Circular(list):
    def __getitem__(self, key):
        return super().__getitem__(key % len(self))

parser = argparse.ArgumentParser(
        description='Calculate the captcha for AoC 2017 day 1')
parser.add_argument('input', metavar='N', type=str, nargs=1)

args = parser.parse_args()

digits = Circular([int(digit) for digit in args.input[0]])

result = 0
for i in range(len(digits)):
    if digits[i] == digits[i + (len(digits) // 2)]:
        result = result + digits[i]

print(result)
