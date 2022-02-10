from os import path

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        heightmap = f.read().splitlines()
    return heightmap

def first(heightmap, directions):
    low_points = []
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
    # print(low_points)
    total = 0
    for low_point in low_points:
        total += 1 + int(low_point)
    print(total)

def solution():
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    heightmap = read_input()
    first(heightmap.copy(), directions)

solution()
