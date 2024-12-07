# https://adventofcode.com/2024/day/7

import re
from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()


def first():
    total = 0
    for line in lines:
        pattern = r"\d+"
        matches = re.findall(pattern, line)
        matches_int = [int(x) for x in matches]
        test_value, eq_list = matches_int[0], matches_int[1:]

        power = len(eq_list) - 1
        for i in range(2**power):
            right_test_value = eq_list[0]
            for j in range(len(eq_list) - 1):
                # 0 - add, 1 - multipley
                if (i >> j) & 1:
                    right_test_value *= eq_list[j + 1]
                else:
                    right_test_value += eq_list[j + 1]
            if right_test_value == test_value:
                total += test_value
                break
    print(total)


def second():
    total = 0
    for line in lines:
        pattern = r"\d+"
        matches = re.findall(pattern, line)
        matches_int = [int(x) for x in matches]
        test_value, eq_list = matches_int[0], matches_int[1:]

        operators = ["+", "*", "c"]

        def compare_test_value(index, right_test_value):
            if index == len(eq_list):
                return right_test_value == test_value
            for i in range(len(operators)):
                operator = operators[i]
                if operator == "+" and compare_test_value(
                    index + 1, right_test_value + eq_list[index]
                ):
                    return True
                elif operator == "*" and compare_test_value(
                    index + 1, right_test_value * eq_list[index]
                ):
                    return True
                elif compare_test_value(
                    index + 1, int(f"{right_test_value}{eq_list[index]}")
                ):
                    return True
                else:
                    pass
            return False

        if compare_test_value(1, eq_list[0]):
            total += test_value

    print(total)


# first()
second()
