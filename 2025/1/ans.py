from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

DIAL_SIZE = 100

def first():
    dial = 50
    counter = 0
    for line in lines:
        direction, value = line[0], int(line[1:])
        value = value % DIAL_SIZE
        if direction == 'L':
            dial = (dial - value + DIAL_SIZE) % DIAL_SIZE
        else:
            dial = (dial + value) % DIAL_SIZE
        if dial == 0:
            counter += 1
    print(counter)

# I had missed the Number at 0 and L5 case, which shouldn't increment the counter
    # Basically for left rotation for a number at 0, I shouldn't increment it if it is less than 0 unless it's a complete rotation
def second():
    dial = 50 # 0
    counter = 0 # 2
    for line in lines:
        direction, value = line[0], int(line[1:])
        rotations = value // DIAL_SIZE # 5 // 100 = 0
        counter += rotations # 0
        mod_value = value % DIAL_SIZE # 5
        if direction == "L":
            if mod_value != 0 and dial != 0 and dial - mod_value <= 0: # 82 - 30 = 52
                counter += 1 # 1
            dial = (dial - mod_value + DIAL_SIZE) % DIAL_SIZE # 52
        else:
            if dial + mod_value >= DIAL_SIZE: # 52 + 48 = 100
                counter += 1
            dial = (dial + mod_value) % DIAL_SIZE
    print(counter)


# first()
second()
