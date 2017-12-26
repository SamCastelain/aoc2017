#!/usr/bin/env python3.6
import argparse

def generator(start, factor):
    value = start

    while True:
        value = (value * factor) % 2147483647
        yield value

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 15')
parser.add_argument('start_a', metavar='start_a', type=int)
parser.add_argument('factor_a', metavar='factor_a', type=int)
parser.add_argument('start_b', metavar='start_b', type=int)
parser.add_argument('factor_b', metavar='factor_b', type=int)

args = parser.parse_args()

gen_a = generator(args.start_a, args.factor_a)
gen_b = generator(args.start_b, args.factor_b)

matches = 0
for i in range(40000000):
    val_a = next(gen_a)
    val_b = next(gen_b)

    if (val_a & 0xFFFF) == (val_b & 0xFFFF):
        matches += 1

print(matches)
