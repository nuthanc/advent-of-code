from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

directions = [
    (-1, -1),  # Top left
    (-1, 0),  # Top
    (-1, 1),  # TR
    (0, 1),  # Right
    (0, -1),  # Left
    (1, -1),  # BL
    (1, 0),  # Bottom
    (1, 1)  # BR
]

rows, cols = len(lines), len(lines[0])


def is_symbol(ch):
    return not ch.isnumeric() and ch != '.'


def is_star_symbol(ch):
    return ch == '*'

def within_bounds(row, col):
    return row >= 0 and row < rows and col >= 0 and col < cols


def first():
    s = 0
    for i in range(rows):
        for j in range(cols):
            ch = lines[i][j]
            if is_symbol(ch):
                end_index = -1
                for row_to_add, col_to_add in directions:
                    if (row_to_add == 0 and col_to_add == 1) or (row_to_add == 0 and col_to_add == -1) or ((row_to_add == 1 and col_to_add == -1)):
                        end_index = -1
                    new_row, new_col = i + row_to_add, j + col_to_add
                    if within_bounds(new_row, new_col) and lines[new_row][new_col].isnumeric() and new_col > end_index:
                        num_col = new_col
                        num = []
                        while num_col >= 0 and lines[new_row][num_col].isnumeric():
                            num_col -= 1
                        num_col += 1
                        while num_col >= 0 and num_col < cols and lines[new_row][num_col].isnumeric():
                            num.append(lines[new_row][num_col])
                            num_col += 1
                        end_index = num_col - 1
                        s += int(''.join(num))
    print(s)

def second():
    s = 0
    for i in range(rows):
        for j in range(cols):
            ch = lines[i][j]
            if is_star_symbol(ch):
                numbers = []
                end_index = -1
                for row_to_add, col_to_add in directions:
                    if (row_to_add == 0 and col_to_add == 1) or (row_to_add == 0 and col_to_add == -1) or ((row_to_add == 1 and col_to_add == -1)):
                        end_index = -1
                    new_row, new_col = i + row_to_add, j + col_to_add
                    if within_bounds(new_row, new_col) and lines[new_row][new_col].isnumeric() and new_col > end_index:
                        num_col = new_col
                        num = []
                        while num_col >= 0 and lines[new_row][num_col].isnumeric():
                            num_col -= 1
                        num_col += 1
                        while num_col >= 0 and num_col < cols and lines[new_row][num_col].isnumeric():
                            num.append(lines[new_row][num_col])
                            num_col += 1
                        end_index = num_col - 1
                        number = int(''.join(num))
                        numbers.append(number)
                if len(numbers) == 2:
                    s += numbers[0] * numbers[1]
    print(s)
                

# first()
second()
