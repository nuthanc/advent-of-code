from os import path
import sys

sys.setrecursionlimit(1500)


THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

directions = (
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
)


def get_score(r, c, last_position_set):
    score = 0
    if lines[r][c] == "9" and (r, c) not in last_position_set:
        score += 1
        last_position_set.add((r, c))
        return score

    for dr, dc in directions:
        new_row, new_col = r + dr, c + dc
        within_bounds = (
            new_row >= 0
            and new_row < len(lines)
            and new_col >= 0
            and new_col < len(lines[0])
        )
        if within_bounds and int(lines[new_row][new_col]) == int(lines[r][c]) + 1:
            score += get_score(new_row, new_col, last_position_set)
    return score


def first():
    total_score = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "0":
                last_position_set = set()
                total_score += get_score(i, j, last_position_set)
                last_position_set.clear()
    print(total_score)


def get_score_second(r, c):
    score = 0
    if lines[r][c] == "9":
        score += 1
        return score

    for dr, dc in directions:
        new_row, new_col = r + dr, c + dc
        within_bounds = (
            new_row >= 0
            and new_row < len(lines)
            and new_col >= 0
            and new_col < len(lines[0])
        )
        if within_bounds and int(lines[new_row][new_col]) == int(lines[r][c]) + 1:
            score += get_score_second(new_row, new_col)
    return score


def second():
    total_score = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "0":
                score = get_score_second(i, j)
                total_score += score
    print(total_score)


# first()
second()
