# Day 2: Password Philosophy: https://adventofcode.com/2020/day/2

# How many passwords are valid
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
    counter = password.count(letter)
    print(lower, higher, letter, password, counter)
    if counter>=int(lower) and counter<=int(higher):
        valid+=1

print(valid)
print(len(passwords))