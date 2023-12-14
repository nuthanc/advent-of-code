from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

report = [list(map(int, line.split())) for line in lines]

def first():
    for line in report:
        print(line)


def second():
    print(report)


first()
