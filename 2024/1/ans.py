# https://adventofcode.com/2024/day/1

from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

first_list, second_list = [], []
for line in lines:
    first, second = line.split('   ')
    first_list.append(int(first))
    second_list.append(int(second))
first_list.sort()
second_list.sort()

second_dict = {}
for item in second_list:
    if item in second_dict:
        second_dict[item] += 1
    else:
        second_dict[item] = 1

def first():
    n = len(first_list)
    s = 0
    for i in range(n):
        diff = abs(first_list[i] - second_list[i])
        s += diff
    print(s)


def second():
    s = 0
    for item in first_list:
        if item in second_dict:
            s += item * second_dict[item]
    print(s)


# first()
second()
