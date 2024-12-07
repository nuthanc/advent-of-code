# https://adventofcode.com/2024/day/5
from os import path
from functools import cmp_to_key

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    input_string = f.read().splitlines()


directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
)

turn_direction = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


def check_within_bounds(new_row, new_col):
    return (
        new_row >= 0
        and new_row < len(input_string)
        and new_col >= 0
        and new_col < len(input_string[0])
    )


visited = [[False] * len(input_string[0]) for _ in range(len(input_string))]
guard_location = []


def first():
    for i in range(len(input_string)):
        for j in range(len(input_string[0])):
            if input_string[i][j] == "^":
                guard_location.append((i, j))
                r, c = i, j
                count = 0
                direction = (-1, 0)
                while check_within_bounds(r, c):
                    if not visited[r][c]:
                        count += 1
                    visited[r][c] = True
                    dx, dy = direction
                    new_row, new_col = r + dx, c + dy
                    within_bounds = check_within_bounds(new_row, new_col)
                    if not within_bounds:
                        break
                    if input_string[new_row][new_col] == "#":
                        tx, ty = turn_direction[(direction[0], direction[1])]
                        r, c, direction = r + tx, c + ty, (tx, ty)
                    else:
                        r, c, direction = new_row, new_col, direction

                print(count)
                break


def second():
    first()
    print("SECOND QUESTION")

    count = 0
    for i in range(len(input_string)):
        for j in range(len(input_string[0])):
            if input_string[i][j] == "." and visited[i][j]:
                r, c = guard_location[0]
                direction = (-1, 0)
                new_visited = [
                    [0] * len(input_string[0]) for _ in range(len(input_string))
                ]
                while check_within_bounds(r, c):
                    if new_visited[r][c] > 4:
                        count += 1
                        break
                    new_visited[r][c] += 1
                    dx, dy = direction
                    new_row, new_col = r + dx, c + dy
                    within_bounds = check_within_bounds(new_row, new_col)
                    if not within_bounds:
                        break
                    if input_string[new_row][new_col] == "#" or (
                        new_row == i and new_col == j
                    ):
                        while input_string[new_row][new_col] == "#" or (
                            new_row == i and new_col == j
                        ):
                            tx, ty = turn_direction[(direction[0], direction[1])]
                            new_row, new_col = r + tx, c + ty
                            direction = (tx, ty)
                        r, c = new_row, new_col
                    else:
                        r, c, direction = new_row, new_col, direction

    print(count)


# first()
second()
# 1889 - Answer too low
