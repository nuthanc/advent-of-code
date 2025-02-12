from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    puzzle_input = f.read()

register_string, program_string = puzzle_input.split('\n\n')
print(register_string)
print(program_string)

def first():
    pass


def second():
    pass


first()
# second()