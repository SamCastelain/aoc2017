#!/usr/bin/env python3.6
import argparse

def execute_spin(programs, number):
    pass


parser = argparse.ArgumentParser(
        description='Solution for part 2 of day 17')
parser.add_argument('steps', metavar='steps', type=int)

args = parser.parse_args()

steps = args.steps
pos = 0

for i in range(1, 50000001):
    pos = ((pos + steps) % i) + 1
    if pos == 1:
        result = i

print(result)
