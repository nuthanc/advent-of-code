# Day 10: Adapter Array: https://adventofcode.com/2020/day/10#part2

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    adapters_string = f.read().splitlines()

adapters = [0]
adapters.extend(list(map(int, adapters_string)))
adapters.sort()
adapters.append((adapters[-1]+3))
# I think BackTracking is a potential solution here
# DP is possible too

def bt(index, adapters, num_arrangements):
    if index == len(adapters)-1:
        num_arrangements[0] += 1
    else:
        for next_jolt in range(1,4):
            try:
                next_index = adapters.index(adapters[index]+next_jolt, index+1, index+4)
            except:
                continue
            else:
                print('next', next_index)
                bt(next_index, adapters, num_arrangements)

num_arrangements = [0]
bt(0, adapters, num_arrangements)
print(num_arrangements[0])
