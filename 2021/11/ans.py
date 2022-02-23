from os import path
from collections import deque

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        energies_string = f.read()
        energies = [[int(energy) for energy in list(line)]
                    for line in energies_string.split('\n')]
    return energies

def bfs(energies, row, col, flashed_set, directions):
    queue = deque()
    queue.append((row,col))
    flashed_set.add((row, col))
    flashes = 0
    while len(queue):
        (row, col) = queue.popleft()
        energies[row][col] = 0
        flashes += 1
        for direction in directions:
            (r, c) = direction
            neighbor_row = row + r
            neighbor_col = col + c
            row_in_range = neighbor_row >= 0 and neighbor_row < len(
                energies)
            col_in_range = neighbor_col >= 0 and neighbor_col < len(
                energies[0])
            if row_in_range and col_in_range:
                if (neighbor_row, neighbor_col) not in flashed_set:
                    energies[neighbor_row][neighbor_col] += 1
                    if energies[neighbor_row][neighbor_col] > 9:
                        flashed_set.add((neighbor_row, neighbor_col))
                        queue.append((neighbor_row, neighbor_col))
    return flashes


def first(energies, directions, steps):
    row_length = len(energies)
    col_length = len(energies[0])
    flashes = 0
    for _ in range(steps):
        flashed_set = set()
        for row in range(row_length):
            for col in range(col_length):
                if (row, col) not in flashed_set:
                    energies[row][col] += 1
                    if energies[row][col] > 9:
                        flashes += bfs(energies, row, col, flashed_set, directions)
    print(flashes)
                    






def solution():
    energies = read_input()
    directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    first(energies.copy(), directions, steps=100)

solution()