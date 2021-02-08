# Day 8: Handheld Halting: https://adventofcode.com/2020/day/8#part2
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    boot_code = f.read().splitlines()

i = 0
acc = 0
visited = set()
op_index = None
opChanged = False
afterChangeAcc = 0
afterChangeVisited = []
while i < len(boot_code):
    if i not in visited:
        visited.add(i)
        op, num = boot_code[i].split(" ")
        num = int(num)
        if op == 'jmp':
            # boot_code[i] = f'nop {num}'
            if not opChanged:
                op_index = (i + num)
                opChanged = not opChanged
                i += 1
            else:
                afterChangeVisited.append(i)
                i = i + num
        elif op == 'nop':
            # boot_code[i] = f'jmp {num}'
            if not opChanged:
                op_index = (i+1)
                i = i + num
                opChanged = not opChanged
            else:
                afterChangeVisited.append(i)
                i += 1
        elif op == 'acc':
            if opChanged:
                afterChangeVisited.append(i)
                afterChangeAcc += num
            acc += num 
            i += 1
    else:
        i = op_index
        op_index = None
        opChanged = False
        acc -= afterChangeAcc
        afterChangeAcc = 0

print(acc)
# IndexError: pop from empty list(Caused by visited, I think)
