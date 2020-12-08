# Report Repair: https://adventofcode.com/2020/day/1#part2

# Find the three entries that sum to 2020
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    expenses_string = f.read().splitlines()

expenses = list(map(int, expenses_string))
expenses.sort()
print(expenses)

for i in range(len(expenses)-3):
    for j in range(i+1, len(expenses)-2):
        for k in range(j+1, len(expenses)-1):
            if(expenses[i]+expenses[j]+expenses[k] == 2020):
                print(expenses[i],expenses[j],expenses[k])
                print(expenses[i]+expenses[j]+expenses[k])
                print(expenses[i]*expenses[j]*expenses[k])
                break