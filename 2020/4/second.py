# Day 4: Passport Processing: https://adventofcode.com/2020/day/4#part2


from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inputs = f.read()

count = 0
passports = inputs.split("\n\n")
req_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    res = all(ele in passport for ele in req_list)
    if res:
        count += 1

print(count)