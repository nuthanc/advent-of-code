from os import path
from collections import deque

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

down_or_up = set([(1, 0), (-1, 0)])
left_or_right = set([(0, -1), (0, 1)])


def first():
    visited = [[False] * len(lines[0]) for _ in range(len(lines))]
    price = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if not visited[i][j]:
                # bfs
                area, perimeter = 0, 0
                q = deque([(i, j)])
                visited[i][j] = True
                while len(q):
                    r, c = q.popleft()
                    area += 1
                    for dr, dc in directions:
                        new_row, new_col = r + dr, c + dc
                        within_bounds = (
                            new_row >= 0
                            and new_row < len(lines)
                            and new_col >= 0
                            and new_col < len(lines[0])
                        )
                        if not within_bounds:
                            perimeter += 1
                        elif lines[r][c] == lines[new_row][new_col]:
                            if not visited[new_row][new_col]:
                                q.append((new_row, new_col))
                                visited[new_row][new_col] = True
                        else:
                            perimeter += 1
                price += area * perimeter
    print(price)


def second():
    visited = [[False] * len(lines[0]) for _ in range(len(lines))]
    price = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if not visited[i][j]:
                # bfs
                area, perimeter = 0, 0
                q = deque([(i, j)])
                visited[i][j] = True
                row_to_direction_map = {}
                col_to_direction_map = {}
                while len(q):
                    r, c = q.popleft()
                    area += 1
                    for dr, dc in directions:
                        new_row, new_col = r + dr, c + dc
                        within_bounds = (
                            new_row >= 0
                            and new_row < len(lines)
                            and new_col >= 0
                            and new_col < len(lines[0])
                        )
                        if not within_bounds:
                            perimeter += get_perimeter(
                                row_to_direction_map, col_to_direction_map, dr, dc, r, c
                            )
                        elif lines[r][c] == lines[new_row][new_col]:
                            if not visited[new_row][new_col]:
                                q.append((new_row, new_col))
                                visited[new_row][new_col] = True
                        else:
                            # todo: Not properly working for this case
                            perimeter += get_perimeter(
                                row_to_direction_map,
                                col_to_direction_map,
                                dr,
                                dc,
                                r,
                                c,
                            )
                print(
                    lines[i][j],
                    area,
                    perimeter,
                )
                print("row_to_direction_map", row_to_direction_map)
                print("col_to_direction_map", col_to_direction_map)
                price += area * perimeter
    print(price)


def get_perimeter(row_to_direction_map, col_to_direction_map, dr, dc, r, c):
    # print('get_perimeter r and c within_bounds', r, c)
    # If there is no entry for that row and that col
    if not row_to_direction_map.get(r) and not col_to_direction_map.get(c):
        if (dr, dc) in down_or_up:
            row_to_direction_map[r] = set([(dr, dc)])
        if (dr, dc) in left_or_right:
            col_to_direction_map[c] = set([(dr, dc)])
        return 1

    add_perimeter = True
    if (
        row_to_direction_map.get(r)
        and (dr, dc) in row_to_direction_map[r]
        # and (not  or (lines[r][c] == lines[r + dr][c + dc]))
    ) or (
        col_to_direction_map.get(c)
        and (dr, dc) in col_to_direction_map[c]
        # and (not  or (lines[r][c] == lines[r + dr][c + dc]))
    ):
        add_perimeter = False

    if row_to_direction_map.get(r):
        if (dr, dc) in down_or_up:
            row_to_direction_map[r].add((dr, dc))
    else:
        if (dr, dc) in down_or_up:
            row_to_direction_map[r] = set([(dr, dc)])

    if col_to_direction_map.get(c):
        if (dr, dc) in left_or_right:
            col_to_direction_map[c].add((dr, dc))
    else:
        if (dr, dc) in left_or_right:
            col_to_direction_map[c] = set([(dr, dc)])

    if add_perimeter:
        return 1
    return 0


# first()
second()
