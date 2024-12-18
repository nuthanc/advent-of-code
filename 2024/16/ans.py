from os import path
import sys

sys.setrecursionlimit(10**6)

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

reverse_directions = {
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
    (0, -1): (0, 1),
    (0, 1): (0, -1),
}

rotate_directions = {
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, 1), (0, -1)],
    (0, 1): [(-1, 0), (1, 0)],
    (0, -1): [(-1, 0), (1, 0)],
}

updated_dict = {}


def dfs(r, c, dr, dc):
    if lines[r][c] == "E":
        return
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
        dfs(new_row, new_col, dr, dc)

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
            ri, rj = reverse_directions[(di, dj)]
            updated_dict[(r, c, ri, rj)] = cost_matrix[r][c] + 1000
            dfs(new_row, new_col, di, dj)


def first():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                cost_matrix[i][j] = 0
                dfs(i, j, 0, 1)  # Starting from East/Right direction
                break
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "E":
                print(cost_matrix[i][j])
                break
    # print(cost_matrix)


visited = [[False] * len(lines[0]) for _ in range(len(lines))]


def dfs_from_end(r, c, dr, dc):
    visited[r][c] = True
    if lines[r][c] == "S":
        return
    new_row, new_col = r + dr, c + dc
    within_bounds = (
        new_row >= 0
        and new_row < len(lines)
        and new_col >= 0
        and new_col < len(lines[0])
    )
    if (cost_matrix[r][c] == 3010 and cost_matrix[new_row][new_col] == 4009):
        print('req', (r, c, dr, dc))
        for key in updated_dict:
            print(key, updated_dict[key])

    if (
        within_bounds
        and lines[new_row][new_col] != "#"
        and (
            (
                cost_matrix[new_row][new_col] < cost_matrix[r][c]
                or (
                    (r, c, dr, dc) in updated_dict
                    and cost_matrix[new_row][new_col] < updated_dict[(r, c, dr, dc)]
                )
            )
            or (
                (new_row, new_col, dr, dc) in updated_dict
                and cost_matrix[r][c] > updated_dict[(new_row, new_col, dr, dc)]
            )
        )
    ):
        dfs_from_end(new_row, new_col, dr, dc)

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
            and (
                (
                    cost_matrix[new_row][new_col] < cost_matrix[r][c]
                    or (
                        (r, c, di, dj) in updated_dict
                        and cost_matrix[new_row][new_col] < updated_dict[(r, c, di, dj)]
                    )
                )
                or (
                    (new_row, new_col, di, dj) in updated_dict
                    and cost_matrix[r][c] > updated_dict[(new_row, new_col, di, dj)]
                )
            )
        ):
            dfs_from_end(new_row, new_col, di, dj)


def second():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                cost_matrix[i][j] = 0
                dfs(i, j, 0, 1)  # Starting from East/Right direction
                break

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "E":
                print("Cost", cost_matrix[i][j])
                dfs_from_end(i, j, 1, 0)
                break
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if visited[i][j]:
                total += 1
    print("Total", total)
    # for key in updated_dict:
    #     print(key, updated_dict[key])


# first()
second()

# [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf ]
# [ inf, 5016, 6017, 6018, 6019, 6020, 6021, 6022,  inf, 9024, 10025, 10026, 10027, 7036,  inf ]
# [ inf, 5015,  inf, 7017,  inf,  inf,  inf, 7023,  inf, 9023,   inf,   inf,   inf, 7035,  inf ]
# [ inf, 5014, 6015, 6016, 6017, 6018,  inf, 7024,  inf, 8022,  8021,  7020,   inf, 7034,  inf ]
# [ inf, 5013,  inf,  inf,  inf, 7019,  inf,  inf,  inf,  inf,   inf,  7019,   inf, 7033,  inf ]
# [ inf, 5012,  inf, 3010,  inf, 6020, 6019, 6018, 6017, 5016,  6017,  6018,   inf, 7032,  inf ]
# [ inf, 5011,  inf, 3009,  inf,  inf,  inf,  inf,  inf, 5015,   inf,   inf,   inf, 7031,  inf ]
# [ inf, 4010, 4009, 3008, 4009, 3010, 4011, 4012, 4013, 4014,  4015,  4016,   inf, 7030,  inf ]
# [ inf,  inf,  inf, 3007,  inf, 3009,  inf,  inf,  inf,  inf,   inf,  5017,   inf, 7029,  inf ]
# [ inf, 1004, 2005, 2006,  inf, 3008, 4009, 4010, 4011, 4012,   inf,  5018,   inf, 7028,  inf ]
# [ inf, 1003,  inf, 3005,  inf, 3007,  inf,  inf,  inf, 5013,   inf,  5019,   inf, 7027,  inf ]
# [ inf, 1002, 2003, 2004, 2005, 2006,  inf, 5012, 6013, 5014,   inf,  5020,   inf, 7026,  inf ]
# [ inf, 1001,  inf,  inf,  inf, 3007,  inf, 5011,  inf, 5013,   inf,  5021,   inf, 7025,  inf ]
# [ inf,    0,    1,    2,  inf, 3008, 4009, 4010, 4011, 4012,   inf,  5022,  6023, 6024,  inf ]
# [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,   inf,   inf,   inf,  inf,  inf ]
