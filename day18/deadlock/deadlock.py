#!/usr/bin/env python3.6
import argparse
from collections import defaultdict
from queue import Queue, Empty

class Program:
    def __init__(self, instructions, program_id):
        self.program_id = program_id
        self.registers = defaultdict(int)
        self.registers['p'] = program_id
        self.send_queue = Queue()
        self.instructions = instructions
        self.pc = 0
        self.number_send = 0
        self.waiting = False

    def set_receive_queue(self, receive_queue):
        self.receive_queue = receive_queue

    def execute(self):
        if not (0 <= self.pc < len(self.instructions)):
            return False

        instruction = self.instructions[self.pc]

        retval = instruction[0](self, *instruction[1])

        if instruction[0] == execute_jump:
            self.pc += retval
        elif instruction[0] == execute_receive and retval == False:
            self.waiting = True
        else:
            if instruction[0] == execute_receive and retval == True:
                self.waiting = False
            self.pc += 1

        return self.waiting

def get_val(registers, operand):
    try:
        val = int(operand)
    except ValueError:
        val = registers[operand]

    return val

def execute_send(program, X):
    val = get_val(program.registers, X)

    program.send_queue.put(val)
    program.number_send += 1

def execute_set(program, X, Y):
    valY = get_val(program.registers, Y)

    program.registers[X] = valY

def execute_add(program, X, Y):
    valY = get_val(program.registers, Y)

    program.registers[X] += valY

def execute_mul(program, X, Y):
    valY = get_val(program.registers, Y)

    program.registers[X] *= valY

def execute_mod(program, X, Y):
    valY = get_val(program.registers, Y)

    program.registers[X] %= valY

def execute_receive(program, X):
    try:
        val = program.receive_queue.get(block=False)
        program.registers[X] = val
        return True
    except Empty:
        return False

def execute_jump(program, X, Y):
    valX = get_val(program.registers, X)
    valY = get_val(program.registers, Y)

    if valX > 0:
        return valY
    else:
        return 1

def compile_instruction(instruction):
    parts = instruction.split()
    if parts[0] == 'snd':
        compiled = (execute_send, (parts[1],))
    elif parts[0] == 'set':
        compiled = (execute_set, (parts[1], parts[2]))
    elif parts[0] == 'add':
        compiled = (execute_add, (parts[1], parts[2]))
    elif parts[0] == 'mul':
        compiled = (execute_mul, (parts[1], parts[2]))
    elif parts[0] == 'mod':
        compiled = (execute_mod, (parts[1], parts[2]))
    elif parts[0] == 'rcv':
        compiled = (execute_receive, (parts[1],))
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

def execute_programs(program0, program1):
    while not program0.waiting or not program1.waiting:
        while True:
            retval = program0.execute()
            if retval:
                program1.execute()
                break
        while True:
            retval = program1.execute()
            if retval:
                program0.execute()
                break

parser = argparse.ArgumentParser(
        description='Solution for part 2 of day 18')
parser.add_argument('file', metavar='file', type=str)

args = parser.parse_args()

compiled = None
with open(args.file) as f:
    compiled = compile_instructions(f)

program0 = Program(compiled, 0)
program1 = Program(compiled, 1)
program0.set_receive_queue(program1.send_queue)
program1.set_receive_queue(program0.send_queue)
execute_programs(program0, program1)
print(program1.number_send)

