from os import path
import heapq


def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        puzzle_input = f.read().splitlines()
    return [list(map(int, list(line))) for line in puzzle_input]


def bellman_ford(row, col, dist_from_src, directions, risk_map):
    for direction in directions:
        r, c = direction
        neighbor_row = row + r
        neighbor_col = col + c
        within_range = neighbor_row >= 0 and neighbor_row < len(
            risk_map) and neighbor_col >= 0 and neighbor_col < len(risk_map[0])
        if within_range:
            new_distance = dist_from_src[row][col] + \
                risk_map[neighbor_row][neighbor_col]
            if new_distance < dist_from_src[neighbor_row][neighbor_col]:
                dist_from_src[neighbor_row][neighbor_col] = new_distance


def first(risk_map, dist_from_src, directions):
    heap = []
    distance = dist_from_src[0][0]
    heapq.heappush(heap, (distance, (0, 0)))
    while len(heap):
        dist, coordinates = heapq.heappop(heap)
        row, col = coordinates
        for direction in directions:
            r, c = direction
            next_row = row + r
            next_col = col + c
            within_bound = next_row >= 0 and next_row < len(
                risk_map) and next_col >= 0 and next_col < len(risk_map[0])
            if within_bound:
                new_dist = dist + risk_map[next_row][next_col]
                if new_dist < dist_from_src[next_row][next_col]:
                    dist_from_src[next_row][next_col] = new_dist
                    heapq.heappush(heap, (new_dist, (next_row, next_col)))


def second(risk_map, directions, grid_size):
    row_len = len(risk_map)
    col_len = len(risk_map[0])
    col_start = grid_size * col_len - col_len
    col_end = grid_size * col_len
    for j in range(grid_size-1):
        for row in range(0, row_len):
            if row + row_len >= len(risk_map):
                risk_map.append(list())
            for col in range(j*col_len, j*col_len+col_len):
                val = risk_map[row][col] + 1
                next_val = 1 if val > 9 else val
                risk_map[row].append(next_val)  # Append to Right Grid
                risk_map[row+row_len].append(next_val)  # Append to Bottom Grid
    for r in range(0, row_len):
        for last_col in range(col_start, col_end):
            val = risk_map[r][last_col] + 1
            next_val = 1 if val > 9 else val
            risk_map[r+row_len].append(next_val)
    for i in range(1,grid_size-1):
        for j in range(0, grid_size):
            for row in range(i*row_len, i*row_len+row_len):
                if row + row_len >= len(risk_map):
                    risk_map.append(list())
                for col in range(j*col_len, j*col_len+col_len):
                    val = risk_map[row][col] + 1
                    next_val = 1 if val > 9 else val
                    risk_map[row+row_len].append(next_val) # Append to Bottom Grid

    dist_from_src = [[float('inf')]*len(risk_map[0])
                     for _ in range(len(risk_map))]
    dist_from_src[0][0] = risk_map[0][0]
    first(risk_map, dist_from_src, directions)
    print(dist_from_src[-1][-1] - risk_map[0][0])

 
def solution():
    risk_map = read_file()
    dist_from_src = [[float('inf')]*len(risk_map[0])
                     for _ in range(len(risk_map))]
    dist_from_src[0][0] = risk_map[0][0]
    directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]
    first(risk_map, dist_from_src, directions) # Used Dijkstra's algorithm(Priority Queue)
    # print(dist_from_src[-1][-1] - risk_map[0][0])
    second(risk_map, directions, 5)


solution()
