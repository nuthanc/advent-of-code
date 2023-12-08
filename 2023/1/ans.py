# https://adventofcode.com/2023/day/1
# Missed this duplicate case: seven6seven, 6one6

from os import path
from re import findall, search

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()


def first():
    s = 0
    for line in lines:
        numbers = findall('\d', line)
        if numbers:
            s += int(numbers[0] + numbers[-1])
    print(s)


def second():
    digits = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    digits_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = 0
    for line in lines:
        numbers = findall('\d', line)
        first_digit = None
        first_digit_index = None
        last_digit = None
        last_digit_index = None
        if numbers:
            first_digit = numbers[0]
            last_digit = numbers[-1]
            first_digit_index = search(first_digit, line).start()
            last_digit_index = line.rfind(last_digit)
        for i in range(len(digits)):
            digit = digits[i]
            match = search(digit, line)
            if match:
                index = match.start()
                if first_digit:
                    if index < first_digit_index:
                        first_digit = digits_num[i]
                        first_digit_index = index
                else:
                    first_digit = digits_num[i]
                    first_digit_index = index

                index = line.rfind(digit)
                if last_digit:
                    if index > last_digit_index:
                        last_digit = digits_num[i]
                        last_digit_index = index
                else:
                    last_digit = digits_num[i]
                    last_digit_index = index
        s += int(first_digit + last_digit)
    print(s)


# first()
second()
