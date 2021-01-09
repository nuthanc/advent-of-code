# Day 8: Handheld Halting: https://adventofcode.com/2020/day/8#part2
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    boot_code = f.read().splitlines()

i = 0
acc = 0
line = set()
while i < len(boot_code):
    if i not in line:
        line.add(i)
        op, num = boot_code[i].split(" ")
        num = int(num)
        if op == 'jmp':
            i = i + num
            if num < 0:
                print(i, num)
            continue
        if op == 'acc':
            acc += num
    else:
        break
    i += 1

print(acc)
# Hint: Think of where the last negative jump occurs