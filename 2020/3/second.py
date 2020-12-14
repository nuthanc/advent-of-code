# Day 3: Password Philosophy: https://adventofcode.com/2020/day/3#part2

# Exactly one of these positions must contain the given letter
from os import path
from numpy import prod

THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    map = f.read().splitlines()

def slope(r, d=1):
    val = 0
    down = d
    right = r
    while down < len(map):
        if map[down][right] == '#':
            val += 1
        right = (right + r) % len(map[0])
        down += d

    return val

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

value_list = []
for value in slopes:
    r, d = value
    value_list.append(slope(r, d))
# print(slope(1,2))

print(slopes)
print(value_list)
print(prod(value_list))
print(len(map), len(map[0]))