# Day 3: Password Philosophy: https://adventofcode.com/2020/day/3

# Exactly one of these positions must contain the given letter
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    map = f.read().splitlines()

val = 0
# For repetition, I can do %len(record)
# for record in map:
#     print(record)

for i in range(1, len(map)):
    slope_index = 3*i%len(map[0])
    if map[i][slope_index] == '#':
        val += 1

print(val)