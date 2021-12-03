# https://adventofcode.com/2021/day/1

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    depths = f.read().splitlines()

depths = list(map(int, depths))
increased = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increased += 1

print(increased)

# Second
prev = float('inf')
window_increased = 0
for i in range(len(depths)):
    if i + 3 <= len(depths):
        window_sum = 0
        for j in range(i,i+3):
            window_sum += depths[j]
        if window_sum > prev:
            window_increased += 1
        prev = window_sum
print(window_increased)