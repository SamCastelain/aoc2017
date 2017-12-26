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

def knot_hash_round(rope, rope_size, lengths, cur_pos, skip_size):
    for length in lengths:
        reverse_elements(rope, rope_size, cur_pos, length)
        cur_pos += length + skip_size
        cur_pos = cur_pos % rope_size
        skip_size += 1

    return cur_pos, skip_size

def knot_hash(string):
    rope = [num for num in range(256)]
    rope = Circular(rope)
    cur_pos = 0
    skip_size = 0

    input_vals = [ord(char) for char in string]
    input_vals.extend([17, 31, 73, 47, 23])

    for _ in range(64):
        cur_pos, skip_size = knot_hash_round(rope, 256, input_vals,
                cur_pos, skip_size)

    dense_hash = [0 for _ in range(16)]
    for i, val in enumerate(rope):
        dense_hash[i // 16] ^= val

    return dense_hash

def count_bits(number):
    count = 0
    while number:
        number &= number - 1
        count += 1

    return count

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 14')
parser.add_argument('key', metavar='key', type=str)

args = parser.parse_args()

key = args.key
grid = []
for i in range(128):
    input_string = key[:] + '-' + str(i)
    grid.append(knot_hash(input_string))

count = 0
for row in grid:
    for number in row:
        count += count_bits(number)

print(count)
