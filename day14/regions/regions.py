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

def is_bit_set(number, column_index):
    mask = 1 << (7 - column_index)
    if (number & mask) == mask:
        return True
    else:
        return False

def convert_to_bitset(number):
    bitset = []
    for i in range(8):
        bitset.append(is_bit_set(number, i))

    return bitset

def generate_grid(key):
    grid = []
    for i in range(128):
        input_string = key[:] + '-' + str(i)
        input_hash = knot_hash(input_string)
        bitset = []
        for number in input_hash:
            bitset.extend(convert_to_bitset(number))
        grid.append(bitset)

    return grid

def dfs_find_group(grid, row, column):
    def is_set(row, column):
        if 0 <= row < 128 and 0 <= column < 128:
            return grid[row][column] == 1
        else:
            return False

    def generate_neighbours(row, column):
        neighbours = [(row + 1, column), (row, column + 1),
                (row - 1, column), (row, column - 1)]

        return [coord for coord in neighbours if is_set(*coord)]

    stack = [(row, column)]
    visited = set()
    while stack:
        coord = stack.pop()
        if coord not in visited:
            visited.add(coord)
            stack.extend(generate_neighbours(*coord))

    return visited

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 14')
parser.add_argument('key', metavar='key', type=str)

args = parser.parse_args()

key = args.key
grid = generate_grid(key)
visited = set()
groups = 0

for row in range(128):
    for column in range(128):
        if grid[row][column]:
            if (row, column) not in visited:
                group = dfs_find_group(grid, row, column)
                visited.update(group)
                groups += 1

print(groups)
