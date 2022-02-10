from os import path

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        heightmap = f.read().splitlines()
    return heightmap

def first(heightmap):
    pass

def solution():
    heightmap = read_input()
    first(heightmap.copy())

solution()
