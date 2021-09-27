# Day 10: Adapter Array: https://adventofcode.com/2020/day/10

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    adapters = f.read().splitlines()

adapters = list(map(int, adapters))
adapters.sort()
adapters.append((adapters[-1]+3))

jolt_diff = {
    1: 0,
    2: 0,
    3: 0
}

jolt_diff[adapters[0]] += 1

for i in range(len(adapters)-1):
    diff = adapters[i+1] - adapters[i]
    jolt_diff[diff] += 1

one_jolt = jolt_diff[1]
three_jolt = jolt_diff[3]
print(one_jolt * three_jolt)
