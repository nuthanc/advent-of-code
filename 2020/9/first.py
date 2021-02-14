# Day 9: Encoding Error: https://adventofcode.com/2020/day/9
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    boot_code = f.read().splitlines()

boot_code = list(map(int, boot_code))

pre_len = 25
pre = set()
found = False
pf_index = 0

for i in range(pre_len):
    pre.add(boot_code[i])

# print(pre)

for i in range(pre_len, len(boot_code)):
    # print(boot_code[i])
    for j in range(pf_index, pf_index+pre_len):
        numToFind = boot_code[i] - boot_code[j]
        if numToFind in pre and numToFind != boot_code[j]:
            found = True
            break
    if found:
        pre.remove(boot_code[pf_index])
        pre.add(boot_code[pf_index+pre_len])
        pf_index += 1
        found = False
    else:
        print(boot_code[i])
        break

