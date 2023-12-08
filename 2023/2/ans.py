from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

s = 0

for line in lines:
    game_str, balls_str = line.split(':')
    _, game_num_str = game_str.split()
    game_sets = balls_str.split(';')
    possible = True
    for game_set in game_sets:
        balls_count = {}
        cubes = game_set.strip().split(',')
        for cube in cubes:
            count_str, color = cube.strip().split(' ')
            balls_count[color] = int(count_str)
        for color_key in bag:
            if color_key in balls_count and bag[color_key] < balls_count[color_key]:
                possible = False
                break
    if possible:
        s += int(game_num_str)

print(s)