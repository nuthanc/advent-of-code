from os import path
from re import search

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    inp = f.read()

directions, nodes = inp.split('\n\n')
nodes_list = nodes.split('\n')
node_map = {}
for node_str in nodes_list:
    result = search('(\w+) = \((\w+), (\w+)\)', node_str)
    key = result.group(1)
    left = result.group(2)
    right = result.group(3)
    node_map[key] = (left, right)

def first():
    n = len(directions)
    i = 0
    steps = 0
    key = 'AAA'
    while key != 'ZZZ':
        index = 0 if directions[i] == 'L' else 1
        key = node_map[key][index]
        steps += 1
        i = (i+1) % n
    print(steps)

# Try for individual ones
def second():
    start_keys = []
    for key in node_map:
        if key[-1] == 'A':
            start_keys.append(key)
    count = len(start_keys)
    n = len(directions)
    i = 0
    steps = 0
    print(start_keys)

    while True:
        li = []
        cur_count = 0
        while len(start_keys):
            key = start_keys.pop()
            index = 0 if directions[i] == 'L' else 1
            node = node_map[key][index]
            li.append(node)
            if node[-1] == 'Z':
                cur_count += 1
        start_keys = li
        steps += 1
        i = (i+1) % n
        if cur_count == count:
            break
    print(steps)



second()
