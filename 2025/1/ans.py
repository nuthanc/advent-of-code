from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()


def first():
    dial = 50
    counter = 0
    for line in lines:
        direction, value = line[0], int(line[1:])
        if direction == 'L':
            dial = (dial - value) % 100
        else:
            dial = (dial + value) % 100
        if dial == 0:
            counter += 1
    print(counter)


def second():
    dial = 50
    counter = 0
    for line in lines:
        direction, value = line[0], int(line[1:])
        if direction == "L":
            dial = (dial - value) % 100
        else:
            dial = (dial + value) % 100
        if dial == 0:
            counter += 1
    print(counter)


first()
# second()
