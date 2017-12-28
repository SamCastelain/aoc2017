#!/usr/bin/env python3.6
import argparse

def execute_spin(programs, number):
    index = len(programs) - number

    new = programs[index:]
    new.extend(programs[:index])
    return new

def execute_exchange(programs, A, B):
    new = programs[:]
    new[A], new[B] = new[B], new[A]

    return new

def execute_partner(programs, A, B):
    new = programs[:]

    for index, program in enumerate(programs):
        if program == A:
            indexA = index
        if program == B:
            indexB = index

    new[indexA], new[indexB] = new[indexB], new[indexA]

    return new

def execute_permutation(programs, permutation):
    if permutation[0] == 's':
        programs = execute_spin(programs, int(permutation[1:]))
    elif permutation[0] == 'x':
        parts = permutation[1:].split('/')
        programs = execute_exchange(programs, int(parts[0]), int(parts[1]))
    elif permutation[0] == 'p':
        parts = permutation[1:].split('/')
        programs = execute_partner(programs, parts[0], parts[1])
    else:
        raise ValueError

    return programs

def execute_permutations(programs, line):
    permutations = line.split(',')

    for permutation in permutations:
        programs = execute_permutation(programs, permutation)

    return programs


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 16')
parser.add_argument('file', metavar='file', type=str)
parser.add_argument('programs', metavar='programs', type=str)

args = parser.parse_args()

programs = list(args.programs)
with open(args.file) as f:
    for line in f:
        result = execute_permutations(programs[:], line.strip())
        print(''.join(result))

