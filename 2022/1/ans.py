# https://adventofcode.com/2022/day/1

from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read()

parsed_strings = lines.split('\n\n')

def first():
    max_calories = 0
    for entry in parsed_strings:
        elf_food = [int(x) for x in entry.split('\n')]
        max_calories = max(max_calories, sum(elf_food))
    print(max_calories)


def second():
    elf_foods_sum = []
    for entry in parsed_strings:
        elf_food = [int(x) for x in entry.split('\n')]
        elf_foods_sum.append(sum(elf_food))
    elf_foods_sum.sort()
    print(elf_foods_sum[-1] + elf_foods_sum[-2] + elf_foods_sum[-3])

# first()
second()
