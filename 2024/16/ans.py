from os import path
from collections import deque

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

cost_matrix = [[float("inf")] * len(lines[0]) for _ in range(len(lines))]

directions = (
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
)

rotate_directions = {
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, 1), (0, -1)],
    (0, 1): [(-1, 0), (1, 0)],
    (0, -1): [(-1, 0), (1, 0)],
}


def bfs(r, c, dr, dc):
    q = deque([(r, c, dr, dc)])
    while len(q):
        r, c, dr, dc = q.popleft()
        if lines[r][c] == "E":
            continue
        new_row, new_col = r + dr, c + dc
        within_bounds = (
            new_row >= 0
            and new_row < len(lines)
            and new_col >= 0
            and new_col < len(lines[0])
        )
        if (
            within_bounds
            and lines[new_row][new_col] != "#"
            and cost_matrix[r][c] + 1 < cost_matrix[new_row][new_col]
        ):
            cost_matrix[new_row][new_col] = cost_matrix[r][c] + 1
            q.append((new_row, new_col, dr, dc))

        for di, dj in rotate_directions[(dr, dc)]:
            new_row, new_col = r + di, c + dj
            within_bounds = (
                new_row >= 0
                and new_row < len(lines)
                and new_col >= 0
                and new_col < len(lines[0])
            )
            if (
                within_bounds
                and lines[new_row][new_col] != "#"
                and cost_matrix[r][c] + 1001 < cost_matrix[new_row][new_col]
            ):
                cost_matrix[new_row][new_col] = cost_matrix[r][c] + 1001
                q.append((new_row, new_col, di, dj))


def first():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                cost_matrix[i][j] = 0
                bfs(i, j, 0, 1)  # Starting from East/Right direction
                break
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "E":
                print(cost_matrix[i][j])
    print(cost_matrix)

def second():
    pass


first()
# second()
