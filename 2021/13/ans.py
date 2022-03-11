from os import path

def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        puzzle_input = f.read()
    return puzzle_input    

def add_to_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key].add(value)
    else:
        dictionary[key] = set([value])

def first(row_dict, col_dict, first_fold):
    _, fold = first_fold.split('fold along ')
    axis, line = fold.split('=')
    line = int(line)
    if axis == 'y':
        for row in list(row_dict):
            if row > line:
                new_key = row - (row - line)*2
                # Migrate values to top
                for value in row_dict[row]:
                    add_to_dict(row_dict, new_key, value)
                    add_to_dict(col_dict, value, new_key)
                    # Remove old row from col_dict
                    col_dict[value].remove(row)
                # Delete old key from row dictionary
                del row_dict[row]
    else:
        for col in list(col_dict):
            if col > line:
                new_key = col - (col - line)*2
                for value in col_dict[col]:
                    add_to_dict(col_dict, new_key, value)
                    add_to_dict(row_dict, value, new_key)
                    # Remove old col from row_dict
                    row_dict[value].remove(col)
                del col_dict[col]
    total_dots = 0 
    for key in row_dict:
        total_dots += len(row_dict[key])
    # print(total_dots)

def second(row_dict, col_dict, instructions):
    for instruction in instructions:
        first(row_dict, col_dict, instruction)
    code = [[] for _ in range(len(row_dict))]
    for key in row_dict:
        for i in range(max(row_dict[key])+1):
            if i in row_dict[key]:
                code[key].append('#')
            else:
                code[key].append('.')
    for line in code:
        print(line)

def solution():
    puzzle_input = read_file()
    dots, instructions = puzzle_input.split('\n\n')
    row_dict = dict()
    col_dict = dict()
    for dot in dots.split('\n'):
        x,y = [int(val) for val in dot.split(',')]
        add_to_dict(row_dict, y, x)
        add_to_dict(col_dict, x, y)
    instructions = instructions.split('\n')
    first(row_dict, col_dict, instructions[0])
    second(row_dict, col_dict, instructions[1:])

solution()