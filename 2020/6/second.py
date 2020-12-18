# Day 6: Custom Customs: https://adventofcode.com/2020/day/6#part2

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inputs = f.read()

count = 0
customs = inputs.split("\n\n")
# print(customs)
for custom in customs:
    # This part is error free
    if '\n' not in custom:
        count += len(custom)
    else:
        uniq = set()
        uniq_dict = {}
        for ele in custom:
            if ele == '\n':
                continue
            if ele in uniq:
                uniq_dict[ele] +=  1
                if uniq_dict[ele] == (custom.count('\n') + 1):
                    count += 1
            else:
                uniq.add(ele)
                uniq_dict[ele] = 1
        # print(uniq_dict)

print(count)