# https://adventofcode.com/2024/day/5

from os import path
from functools import cmp_to_key

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    input_string = f.read()

ordering_input, updates_input = input_string.split('\n\n')

ordering_list = ordering_input.splitlines()
updates_list = [line.split(',') for line in updates_input.splitlines()]

order_dict = {}
for line in ordering_list:
    first, second = [int(x) for x in line.split("|")]
    order_dict[(first, second)] = -1
    order_dict[(second, first)] = 1

def check_order(line):
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            first, second = int(line[i]), int(line[j])
            if order_dict[(first, second)] == 1:
                return False
    return True

def first():
    total = 0
    for line in updates_list:
        if check_order(line):
            total += int(line[len(line) // 2])
    print(total)


def check_order_second(line):
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            first, second = int(line[i]), int(line[j])
            if order_dict[(first, second)] == 1:
                return True
    return False

def my_sort(a,b):
    return order_dict[(int(a),int(b))]

def second():
    print("SECOND QUESTION")
    total = 0
    for line in updates_list:
        if check_order_second(line):
            line.sort(key=cmp_to_key(my_sort))
            total += int(line[len(line) // 2])
    print(total)

# first()
second()
