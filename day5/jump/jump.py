#!/usr/bin/env python3.6
import argparse
import sys

parser = argparse.ArgumentParser(
        description='Soltion for part 1 of day 5')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

tape = []
with open(args.file[0]) as f:
    for line in f:
        tape.append(int(line))

steps = 0
index = 0
length = len(tape)
while index >= 0 and index < length:
    offset = tape[index]
    tape[index] += 1
    index += offset
    steps += 1

print(steps)
