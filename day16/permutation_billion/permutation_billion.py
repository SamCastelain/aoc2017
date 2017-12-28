#!/usr/bin/env python3.6
import argparse

def execute_spin(programs, number):
    index = len(programs) - number

    new = programs[index:]
    new.extend(programs[:index])
    return new

def execute_exchange(programs, A, B):
    programs[A], programs[B] = programs[B], programs[A]

    return programs

def execute_partner(programs, A, B):
    new = programs[:]

    for index, program in enumerate(programs):
        if program == A:
            indexA = index
        if program == B:
            indexB = index

    programs[indexA], programs[indexB] = programs[indexB], programs[indexA]

    return programs

def compile_permutation(permutation):
    if permutation[0] == 's':
        compiled = (execute_spin, (int(permutation[1:]),))
    elif permutation[0] == 'x':
        parts = permutation[1:].split('/')
        compiled = (execute_exchange, (int(parts[0]), int(parts[1])))
    elif permutation[0] == 'p':
        parts = permutation[1:].split('/')
        compiled = (execute_partner, (parts[0], parts[1]))
    else:
        raise ValueError

    return compiled

def compile_permutations(line):
    permutations = line.split(',')
    compiled = []
    for permutation in permutations:
        compiled.append(compile_permutation(permutation))

    return compiled

def execute_permutations(programs, compiled_permutations):

    for compiled_perm in compiled_permutations:
        programs = compiled_perm[0](programs, *compiled_perm[1])

    return programs


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 16')
parser.add_argument('file', metavar='file', type=str)
parser.add_argument('programs', metavar='programs', type=str)

args = parser.parse_args()

programs = list(args.programs)
with open(args.file) as f:
    for line in f:
        compiled = compile_permutations(line.strip())
        iterations = 0
        work_copy = programs[:]
        while (work_copy != programs) or (iterations == 0):
            work_copy = execute_permutations(work_copy, compiled)
            iterations += 1

        count = 1000000000 % iterations
        for _ in range(count):
            work_copy = execute_permutations(work_copy, compiled)
        print(''.join(work_copy))

