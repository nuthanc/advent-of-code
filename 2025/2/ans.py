# https://adventofcode.com/2025/day/2
from os import path
from math import sqrt

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    line = f.read()

# Even length digits only, split in middle and first half and second half is the same
ranges = line.split(',')

def first():
    s = 0
    for r in ranges:
        first_string, second_string = r.split('-')
        first_number, second_number = int(first_string), int(second_string)
        for num in range(first_number, second_number+1):
            num_string = str(num)
            num_string_length = len(num_string)
            half_length = num_string_length // 2
            if num_string_length % 2 == 0:
                if num_string[:half_length] == num_string[half_length:]:
                    s += int(num_string)
    print(s)

def is_palindrome(num_string, num_length):
    i, j = 0, num_length-1

    while i < j:
        if num_string[i] != num_string[j]:
            return False
        i += 1
        j -= 1
    return True


def second():
    s = 0
    for r in ranges:
        first_string, second_string = r.split("-")
        first_number, second_number = int(first_string), int(second_string)
        for num in range(first_number, second_number + 1):
            num_string = str(num)
            num_string_length = len(num_string)
            if is_palindrome(num_string, num_string_length):
                s += int(num_string)
                continue

            for i in range(2, int(sqrt(num_string_length))):
                if num_string_length % i != 0:
                    continue
                factors = [i, num_string_length // i]
                for factor in factors:
                    


# first()
second()
