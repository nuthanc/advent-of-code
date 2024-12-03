from os import path
import re

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    instructions = f.read()


def first(instructions):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, instructions)
    s = 0
    for match in matches:
        numbers = [int(x) for x in re.findall(r"\d+", match)]
        s += numbers[0] * numbers[1]
    print(s)


def second():
    print("SECOND QUESTION")
    do_instructions = ''
    do_sections = instructions.split("do()")
    for section in do_sections:
        do_instructions += section.split("don't()")[0]
    first(do_instructions)


# first(instructions)
second()
