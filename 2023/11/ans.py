from os import path
from collections import deque

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

expanded_rows, expanded_cols = set(), set()
space, galaxy = '.', '#'
col_count = len(lines[0])
row_count = len(lines)
directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def check_expanded_rows():
    for row_index, row in enumerate(lines):
        cur_count = 0
        for col in row:
            if col == space:
                cur_count += 1
        if cur_count == col_count:
            expanded_rows.add(row_index)


def check_expanded_cols():
    for i in range(col_count):
        cur_count = 0
        for j in range(row_count):
            if lines[j][i] == space:
                cur_count += 1
        if cur_count == row_count:
            expanded_cols.add(i)

def bfs(row, col, expansion):
    q = deque([(row, col, 0)])
    visited = [[False] * col_count for _ in range(row_count)]
    visited[row][col] = True
    s = 0
    while len(q):
        r, c, w = q.popleft()
        for row_offset, col_offset in directions:
            next_row, next_col = r + row_offset, c + col_offset
            within_bounds = next_row >= 0 and next_row < row_count and next_col >= 0 and next_col < col_count
            if within_bounds and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                weight_to_add = expansion if next_row in expanded_rows or next_col in expanded_cols else 1
                weight = w + weight_to_add
                if lines[next_row][next_col] == galaxy:
                    s += weight
                q.append((next_row, next_col, weight))
    return s



def first():
    check_expanded_rows()
    check_expanded_cols()
    # Apply bfs with sequential traversal
    s = 0
    for i in range(row_count):
        for j in range(col_count):
            if lines[i][j] == galaxy:
               s += bfs(i, j, 2)
    print(s // 2)


def second():
    check_expanded_rows()
    check_expanded_cols()
    # Apply bfs with sequential traversal
    s = 0
    for i in range(row_count):
        for j in range(col_count):
            if lines[i][j] == galaxy:
               s += bfs(i, j, 1000000)
    print(s // 2)


second()
