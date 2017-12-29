#!/usr/bin/env python3.6
import argparse

def execute_spin(programs, number):
    pass


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 17')
parser.add_argument('steps', metavar='steps', type=int)

args = parser.parse_args()

steps = args.steps
buf = [0]
pos = 0

for i in range(1, 2018):
    pos = ((pos + steps) % i) + 1
    buf.insert(pos, i)

print(buf[(pos + 1) % 2018])
