# Day 4: Passport Processing: https://adventofcode.com/2020/day/4#part2

import re
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inputs = f.read()

passports = inputs.split("\n\n")

def byr_cond(byr):
    if len(byr) == 4:
        byr = int(byr)
        if byr >= 1920 and byr <=2002:
            return True
        else:
            return False
    else:
        return False

def iyr_cond(iyr):
    if len(iyr) == 4:
        iyr = int(iyr)
        if iyr >= 2010 and iyr <=2020:
            return True
        else:
            return False
    else:
        return False

def eyr_cond(eyr):
    if len(eyr) == 4:
        eyr = int(eyr)
        if eyr >= 2020 and eyr <=2030:
            return True
        else:
            return False
    else:
        return False

def hgt_cond(hgt):
    if 'cm' in hgt:
        num = int(hgt.split('cm')[0])
        if num >=150 and num<= 193:
            return True
        else:
            return False
    elif 'in' in hgt:
        num = int(hgt.split('in')[0])
        if num >=59 and num<= 76:
            return True
        else:
            return False
    else:
        return False

def hcl_cond(hcl):
    if '#' in hcl:
        hcl = hcl.split('#')[1]
        if len(hcl) == 6:
            pattern = re.compile("[a-f0-9]+")
            if pattern.fullmatch(hcl) is not None:
                return True
            else:
                return False
        return False
    return False

def ecl_cond(ecl):
    colors = ['amb', 'brn', 'blu', 'gry', 'grn', 'hzl', 'oth']
    if ecl in colors:
        return True
    return False

def pid_cond(pid):
    if len(pid) == 9:
        return True
    return False

req_dict = {'byr': byr_cond, 'iyr': iyr_cond, 'eyr': eyr_cond, 'hgt': hgt_cond, 'hcl': hcl_cond, 'ecl': ecl_cond, 'pid': pid_cond}
valid = 0
for passport in passports:
    res = all(ele in passport for ele in req_dict.keys())
    if res:
        count = 0
        d = dict(p.split(':') for p in re.split('[\s\n]',passport))
        for k,v in d.items():
            if k == 'cid':
                continue
            if req_dict[k](v):
                # print(f'{k}:{v} is valid')
                count += 1
            else:
                # print(f'{k}:{v} is INVALID')
                break
        if count == 7:
            valid += 1
print(valid)