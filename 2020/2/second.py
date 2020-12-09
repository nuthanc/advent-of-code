# Day 2: Password Philosophy: https://adventofcode.com/2020/day/2#part2

# Exactly one of these positions must contain the given letter
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    passwords = f.read().splitlines()

valid = 0
for p in passwords:
    times, letterc, password = p.split(" ")
    lower, higher = times.split("-")
    letter = letterc.split(":")[0]
    # print(lower, higher, letter, password)
    if (password[int(lower)-1] == letter) != (password[int(higher)-1] == letter):
        valid += 1
        print(lower, higher, letter, password)
    else:
        print(f'Invalid: {lower} {higher} {letter} {password}')

print(valid)
print(len(passwords))
