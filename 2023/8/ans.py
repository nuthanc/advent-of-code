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


def second():
    pass


first()
