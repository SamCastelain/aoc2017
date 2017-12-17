#!/usr/bin/env python3.6
import argparse

class Circular(list):
    def __getitem__(self, key):
        return super().__getitem__(key % len(self))

    def __setitem__(self, key, value):
        return super().__setitem__(key % len(self), value)

def reverse_elements(rope, rope_size, cur_pos, length):
    for i in range(length // 2):
        index0 = cur_pos + i
        index1 = cur_pos + (length - 1 - i)

        rope[index0], rope[index1] = rope[index1], rope[index0]

def knot_hash(line, rope_size):
    rope = [num for num in range(rope_size)]
    rope = Circular(rope)
    cur_pos = 0
    skip_size = 0

    for length in line.split(','):
        length = int(length.strip())
        reverse_elements(rope, rope_size, cur_pos, length)
        cur_pos += length + skip_size
        cur_pos = cur_pos % rope_size
        skip_size += 1

    return rope[0] * rope[1]

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 10')
parser.add_argument('file', metavar='file', type=str)
parser.add_argument('size', metavar='size', type=int)

args = parser.parse_args()

with open(args.file) as f:
    for line in f:
        value = knot_hash(line, args.size)
        print(value)
