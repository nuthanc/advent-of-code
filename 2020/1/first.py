# Report Repair: https://adventofcode.com/2020/day/1

# Find the two entries that sum to 2020
with open('input.txt') as f:
    expenses_string = f.read().splitlines()

expenses = list(map(int, expenses_string))
expenses.sort()
print(expenses)

start_index = 0
end_index = len(expenses) - 1
sum = expenses[start_index] + expenses[end_index]
# import pdb;pdb.set_trace()
while sum != 2020:
    if sum > 2020:
        end_index -= 1
    elif sum < 2020:
        start_index +=1
    else:
        break
    sum = expenses[start_index] + expenses[end_index]
    # print(expenses[start_index], expenses[end_index], sum)


print(expenses[start_index], expenses[end_index])
print(expenses[start_index]*expenses[end_index])
