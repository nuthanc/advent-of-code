# https://adventofcode.com/2024/day/4

from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

# Right, Bottom Right, Bottom, Bottom Left, Left, Top Left, Top, Top Right
directions = (
    (0, 1, "R"),
    (1, 1, "BR"),
    (1, 0, "B"),
    (1, -1, "BL"),
    (0, -1, "L"),
    (-1, -1, "TL"),
    (-1, 0, "T"),
    (-1, 1, "TR"),
)

desired = ("X", "M", "A", "S")


def search(x, y, index, search_direction):
    count = 0
    if index == len(desired):
        return 1
    if search_direction == "A":
        for dx, dy, direction in directions:
            row, col = x + dx, y + dy
            within_bounds = (
                row >= 0 and row < len(lines) and col >= 0 and col < len(lines[0])
            )
            if within_bounds and lines[row][col] == desired[index]:
                count += search(row, col, index + 1, direction)
    else:
        i, j = None, None
        for dx, dy, direction in directions:
            if direction == search_direction:
                i, j = dx, dy
                break
        row, col = x + i, y + j
        within_bounds = (
            row >= 0 and row < len(lines) and col >= 0 and col < len(lines[0])
        )
        if within_bounds and lines[row][col] == desired[index]:
            count += search(row, col, index + 1, search_direction)
    return count


def first():
    total = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            ch = line[j]
            if ch == desired[0]:
                total += search(i, j, 1, "A")
    print(total)


def search_second(x, y, ch):
    if ch == "M" and (
        (y + 2 < len(lines[0]) and lines[x][y + 2] == "S")
        and (
            x + 1 < len(lines) and y + 1 < len(lines[0]) and lines[x + 1][y + 1] == "A"
        )
        and (x + 2 < len(lines) and lines[x + 2][y] == "M")
        and (
            x + 2 < len(lines) and y + 2 < len(lines[0]) and lines[x + 2][y + 2] == "S"
        )
    ):
        return 1
    if ch == "M" and (
        (y + 2 < len(lines[0]) and lines[x][y + 2] == "M")
        and (
            x + 1 < len(lines) and y + 1 < len(lines[0]) and lines[x + 1][y + 1] == "A"
        )
        and (x + 2 < len(lines) and lines[x + 2][y] == "S")
        and (
            x + 2 < len(lines) and y + 2 < len(lines[0]) and lines[x + 2][y + 2] == "S"
        )
    ):
        return 1
    if ch == "S" and (
        (y + 2 < len(lines[0]) and lines[x][y + 2] == "S")
        and (
            x + 1 < len(lines) and y + 1 < len(lines[0]) and lines[x + 1][y + 1] == "A"
        )
        and (x + 2 < len(lines) and lines[x + 2][y] == "M")
        and (
            x + 2 < len(lines) and y + 2 < len(lines[0]) and lines[x + 2][y + 2] == "M"
        )
    ):
        return 1
    if ch == "S" and (
        (y + 2 < len(lines[0]) and lines[x][y + 2] == "M")
        and (
            x + 1 < len(lines) and y + 1 < len(lines[0]) and lines[x + 1][y + 1] == "A"
        )
        and (x + 2 < len(lines) and lines[x + 2][y] == "S")
        and (
            x + 2 < len(lines) and y + 2 < len(lines[0]) and lines[x + 2][y + 2] == "M"
        )
    ):
        return 1
    return 0


def second():
    print("SECOND QUESTION")
    total = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            ch = line[j]
            if ch == "M":
                total += search_second(i, j, "M")
            if ch == "S":
                total += search_second(i, j, "S")
    print(total)


# first()
second()
