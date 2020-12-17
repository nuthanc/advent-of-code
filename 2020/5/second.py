# Day 5: Binary Boarding: https://adventofcode.com/2020/day/5#part2

import sys
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    passes = f.read().splitlines()

max = 0
min = 0
id_list = []
for p in passes:
    # row_ind = p[0:7]
    # seat_ind = p[-3:]
    row_low = 0
    row_high = 127
    col_low = 0
    col_high = 7
    for ch in p:
        if ch == 'F':
            row_high = (row_low + row_high)//2
        if ch == 'B':
            row_low = (row_low + row_high)//2 + 1
        if ch == 'L':
            col_high = (col_low + col_high)//2
        if ch == 'R':
            col_low = (col_low + col_high)//2 + 1
    row = row_low
    col = col_low
    # print(row, col)
    id = row*8 + col
    # print(id)
    id_list.append(id)
    if id > max:
        max = id
    if id < min:
        min = id
print("max id:", max)
print("min id:", min)
id_list.sort()


# A binary search based recursive function
# that returns the missing element in
# arithmetic progression
# https://www.geeksforgeeks.org/find-missing-number-arithmetic-progression/
def findMissingUtil(arr, low, high, diff):

    # There must be two elements to
    # find the missing
    if (high <= low):
        return sys.maxsize

    # Find index of middle element
    mid = int(low + (high - low) / 2)

    # The element just after the middle
    # element is missing. The arr[mid+1]
    # must exist, because we return when
    # (low == high) and take floor of
    # (high-low)/2
    if (arr[mid + 1] - arr[mid] != diff):
        return (arr[mid] + diff)

    # The element just before mid is missing
    if (mid > 0 and arr[mid] -
            arr[mid - 1] != diff):
        return (arr[mid - 1] + diff)

    # If the elements till mid follow AP,
    # then recur for right half
    if (arr[mid] == arr[0] + mid * diff):
        return findMissingUtil(arr, mid + 1,
                               high, diff)

    # Else recur for left half
    return findMissingUtil(arr, low,
                           mid - 1, diff)

# The function uses findMissingUtil() to find
# the missing element in AP. It assumes that
# there is exactly one missing element and may
# give incorrect result when there is no missing
# element or more than one missing elements.
# This function also assumes that the difference
# in AP is an integer.


def findMissing(arr, n):

    # If exactly one element is missing, then
    # we can find difference of arithmetic
    # progression using following formula.
    # Example, 2, 4, 6, 10, diff = (10-2)/4 = 2.
    # The assumption in formula is that the
    # difference is an integer.
    diff = int((arr[n - 1] - arr[0]) / n)

    # Binary search for the missing number
    # using above calculated diff
    return findMissingUtil(arr, 0, n - 1, diff)


n = len(id_list)
print("The missing element is",
      findMissing(id_list, n))
