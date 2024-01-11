from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inp = f.read()

raw_patterns = inp.split('\n\n')
patterns = []
for pattern in raw_patterns:
    patterns.append(pattern.split('\n'))

'''
# Constraints

* More than 1 line of reflection(like vertical and horizontal in a single pattern)
    * Initial implementation consider only 1 per pattern
# Break down and Simplify

* Find line of reflection in a pattern
* Reflection line can be vertical or horizontal
* Vertical: Same count of ash and rocks and same position
'''


def compare_rows(col_len, pattern, row, next_row):
    identical = True
    for c in range(col_len):
        if pattern[row][c] != pattern[next_row][c]:
            identical = False
            break
    return identical


def check_horizontal_reflection(pattern):
    row_len, col_len = len(pattern), len(pattern[0])
    for row in range(row_len-1):
        next_row = row+1
        identical = compare_rows(col_len, pattern, row, next_row)
        if identical:
            r1, r2 = row - 1, next_row + 1
            within_bounds = r1 >= 0 and r2 < row_len
            is_reflection = True
            while within_bounds:
                identical = compare_rows(col_len, pattern, r1, r2)
                if not identical:
                    is_reflection = False
                    break
                r1, r2 = r1 - 1, r2 + 1
                within_bounds = r1 >= 0 and r2 < row_len
            if is_reflection:
                return row + 1
    return 0


def compare_cols(row_len, pattern, col, next_col):
    identical = True
    for r in range(row_len):
        if pattern[r][col] != pattern[r][next_col]:
            identical = False
            break
    return identical


def check_vertical_reflection(pattern):
    row_len, col_len = len(pattern), len(pattern[0])
    for col in range(col_len-1):
        next_col = col+1
        identical = compare_cols(row_len, pattern, col, next_col)
        if identical:
            c1, c2 = col - 1, next_col + 1
            within_bounds = c1 >= 0 and c2 < col_len
            is_reflection = True
            while within_bounds:
                identical = compare_cols(row_len, pattern, c1, c2)
                if not identical:
                    is_reflection = False
                    break
                c1, c2 = c1 - 1, c2 + 1
                within_bounds = c1 >= 0 and c2 < col_len
            if is_reflection:
                return col + 1
    return 0


def first():
    rows, cols = 0, 0
    for pattern in patterns:
        rows += check_horizontal_reflection(pattern)
        cols += check_vertical_reflection(pattern)
    print(100 * rows + cols)


def compare_rows_second(col_len, pattern, row, next_row):
    identical = True
    smudges = 0
    for c in range(col_len):
        if pattern[row][c] != pattern[next_row][c]:
            if smudges == 0:
                smudges = 1
                continue
            identical = False
            break
    return identical, smudges


def check_horizontal_reflection_second(pattern):
    row_len, col_len = len(pattern), len(pattern[0])
    for row in range(row_len-1):
        smudges = 0
        next_row = row+1
        identical, smudges_row = compare_rows_second(
            col_len, pattern, row, next_row)
        smudges += smudges_row
        if identical:
            r1, r2 = row - 1, next_row + 1
            within_bounds = r1 >= 0 and r2 < row_len
            is_reflection = True
            while within_bounds and smudges <= 1:
                identical, smudges_row = compare_rows_second(
                    col_len, pattern, r1, r2)
                smudges += smudges_row
                if not identical:
                    is_reflection = False
                    break
                r1, r2 = r1 - 1, r2 + 1
                within_bounds = r1 >= 0 and r2 < row_len
            if is_reflection and smudges == 1:
                return row + 1
    return 0


def compare_cols_second(row_len, pattern, col, next_col):
    identical = True
    smudges = 0
    for r in range(row_len):
        if pattern[r][col] != pattern[r][next_col]:
            if smudges == 0:
                smudges = 1
                continue
            identical = False
            break
    return identical, smudges


def check_vertical_reflection_second(pattern):
    row_len, col_len = len(pattern), len(pattern[0])
    for col in range(col_len-1):
        smudges = 0
        next_col = col+1
        identical, smudges_col = compare_cols_second(row_len, pattern, col, next_col)
        smudges += smudges_col
        if identical:
            c1, c2 = col - 1, next_col + 1
            within_bounds = c1 >= 0 and c2 < col_len
            is_reflection = True
            while within_bounds and smudges <= 1:
                identical, smudges_col = compare_cols_second(row_len, pattern, c1, c2)
                smudges += smudges_col
                if not identical:
                    is_reflection = False
                    break
                c1, c2 = c1 - 1, c2 + 1
                within_bounds = c1 >= 0 and c2 < col_len
            if is_reflection and smudges == 1:
                return col + 1
    return 0


def second():
    rows, cols = 0, 0
    for pattern in patterns:
        rows += check_horizontal_reflection_second(pattern)
        cols += check_vertical_reflection_second(pattern)
    print(100 * rows + cols)


second()
