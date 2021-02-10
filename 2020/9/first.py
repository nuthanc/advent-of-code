# Day 9: Encoding Error: https://adventofcode.com/2020/day/9
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    boot_code = f.read().splitlines()

pre_len = 5
pre = set()

for i in range(pre_len):
    pre.add(boot_code[i])

print(pre)

for i in range(pre_len, len(boot_code)):
    print(boot_code[i])