# Day 5: Binary Boarding: https://adventofcode.com/2020/day/5

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    passes = f.read().splitlines()

max = 0
for p in passes:
    # row_ind = p[0:7]
    # seat_ind = p[-3:]
    row_low = 0
    row_high = 127
    col_low = 0
    col_high = 7
    for ch in p:
        if ch == 'F':
            row_high = (row_low + row_high)//2
        if ch == 'B':
            row_low = (row_low + row_high)//2 + 1
        if ch == 'L':
            col_high = (col_low + col_high)//2
        if ch == 'R':
            col_low = (col_low + col_high)//2 + 1
    row = row_low
    col = col_low
    # print(row, col)
    id = row*8 + col
    # print(id)
    if id > max:
        max = id
    if id < min:
        min = id

print("max id:", max)