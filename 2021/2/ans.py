# https://adventofcode.com/2021/day/2

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    instructions = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0

def first(horizontal, depth):
    for instruction in instructions:
        direction, val = instruction.split()
        val = int(val)
        if direction == 'forward':
            horizontal += val
        elif direction == 'up':
            depth -= val
        else:
            depth += val
    print(horizontal * depth)

# first(horizontal, depth)

# Part 2

def second(horizontal, depth, aim):
    for instruction in instructions:
        direction, val = instruction.split()
        val = int(val)
        
        if direction == 'forward':
            horizontal += val
            depth += aim * val
        elif direction == 'up':
            aim -= val
        else:
            aim += val
    print(horizontal * depth)
    
second(horizontal, depth, aim)
