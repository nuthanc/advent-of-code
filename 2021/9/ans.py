from os import path

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        heightmap = f.read().splitlines()
    return heightmap

def first(heightmap, directions):
    low_points = []
    low_points_coordinates = []
    for row, heights in enumerate(heightmap):
        for col, height in enumerate(heights):
            is_low_point = True
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row >=0 and new_row < len(heightmap) and new_col >=0 and new_col < len(heights):
                    surronding_height = heightmap[new_row][new_col]
                    if height >= surronding_height:
                        is_low_point = False
                        break
            if is_low_point:
                low_points.append(height)
                low_points_coordinates.append((row, col))
    # print(low_points)
    total = 0
    for low_point in low_points:
        total += 1 + int(low_point)
    # print(total)
    return low_points_coordinates


def dfs(row, col, heightmap, directions, seen, size):
    seen.add((row, col))
    for direction in directions:
        neighbor_row = row + direction[0]
        neighbor_col = col + direction[1]
        within_bounds = neighbor_row >=0 and neighbor_row < len(heightmap) and neighbor_col >=0 and neighbor_col < len(heightmap[0])
        not_seen = (neighbor_row, neighbor_col) not in seen
        if  within_bounds and not_seen and heightmap[neighbor_row][neighbor_col] != '9':
            neighbor = heightmap[neighbor_row][neighbor_col]
            current = heightmap[row][col]
            if neighbor > current:
                size += dfs(neighbor_row, neighbor_col, heightmap, directions, seen, 1)
    return size


def second(heightmap, directions):
    low_points_coordinates = first(heightmap, directions)
    seen = set()
    basins = []
    for coordinate in low_points_coordinates:
        (row, col) = coordinate
        basin_size = dfs(row, col, heightmap, directions, seen, size=1)
        basins.append(basin_size)
    basins.sort(reverse=True)
    product_of_3_largest_basins = basins[0] * basins[1] * basins[2]
    print(product_of_3_largest_basins)

def solution():
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    heightmap = read_input()
    second(heightmap, directions)

solution()
