# Day 9: Encoding Error: https://adventofcode.com/2020/day/9#part2
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
invalid_num = None

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
        invalid_num = boot_code[i]
        print("Invalid number", boot_code[i])
        break

for i in range(len(boot_code)-1):
    sum = boot_code[i]
    smallest = boot_code[i]
    largest = boot_code[i]
    for j in range(i+1, len(boot_code)):
        smallest = min(boot_code[j], smallest)
        largest = max(boot_code[j], largest)
        sum += boot_code[j]
        if sum > invalid_num:
            break
        if sum == invalid_num:
            print("Smallest + Largest", smallest+largest)
            
