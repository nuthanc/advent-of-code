# Day 6: Custom Customs: https://adventofcode.com/2020/day/6

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inputs = f.read()

count = 0
customs = inputs.split("\n\n")
for custom in customs:
    custom = custom.replace('\n','')
    # print(custom)
    count += len(set(custom))

print(count)