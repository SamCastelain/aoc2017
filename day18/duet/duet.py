#!/usr/bin/env python3.6
import argparse
from collections import defaultdict

class SoundCard:
    def __init__(self):
        self.registers = defaultdict(int)
        self.last_played = 0

def get_val(registers, operand):
    try:
        val = int(operand)
    except ValueError:
        val = registers[operand]

    return val

def execute_sound(soundcard, X):
    val = get_val(soundcard.registers, X)

    soundcard.last_played = val

def execute_set(soundcard, X, Y):
    valY = get_val(soundcard.registers, Y)

    soundcard.registers[X] = valY

def execute_add(soundcard, X, Y):
    valY = get_val(soundcard.registers, Y)

    soundcard.registers[X] += valY

def execute_mul(soundcard, X, Y):
    valY = get_val(soundcard.registers, Y)

    soundcard.registers[X] *= valY

def execute_mod(soundcard, X, Y):
    valY = get_val(soundcard.registers, Y)

    soundcard.registers[X] %= valY

def execute_recover(soundcard, X):
    val = get_val(soundcard.registers, X)

    if val != 0:
        return soundcard.last_played
    else:
        return None

def execute_jump(soundcard, X, Y):
    valX = get_val(soundcard.registers, X)
    valY = get_val(soundcard.registers, Y)

    if valX > 0:
        return valY
    else:
        return 1

def compile_instruction(instruction):
    parts = instruction.split()
    if parts[0] == 'snd':
        compiled = (execute_sound, (parts[1],))
    elif parts[0] == 'set':
        compiled = (execute_set, (parts[1], parts[2]))
    elif parts[0] == 'add':
        compiled = (execute_add, (parts[1], parts[2]))
    elif parts[0] == 'mul':
        compiled = (execute_mul, (parts[1], parts[2]))
    elif parts[0] == 'mod':
        compiled = (execute_mod, (parts[1], parts[2]))
    elif parts[0] == 'rcv':
        compiled = (execute_recover, (parts[1],))
    elif parts[0] == 'jgz':
        compiled = (execute_jump, (parts[1], parts[2]))
    else:
        raise ValueError

    return compiled

def compile_instructions(f):
    compiled = []
    for line in f:
        compiled.append(compile_instruction(line.strip()))

    return compiled

def execute_instructions(soundcard, program):
    i = 0

    while 0 <= i < len(program):
        instruction = program[i]

        retval = instruction[0](soundcard, *instruction[1])

        if instruction[0] == execute_jump:
            i += retval
        elif instruction[0] == execute_recover and retval is not None:
            return retval
        else:
            i += 1

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 18')
parser.add_argument('file', metavar='file', type=str)

args = parser.parse_args()

compiled = None
with open(args.file) as f:
    compiled = compile_instructions(f)

soundcard = SoundCard()
print(execute_instructions(soundcard, compiled))

