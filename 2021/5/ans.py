'''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....


0,9 -> 5,9
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
0,9 -> 2,9
3,4 -> 1,4

# Constraints:

1. Verify the Constraints
* Horizontal and vertical lines, i.e x1=x2 or y1=y2

2. Write some test cases

3. Solution without code
* Read the input as list of strings
* Initialize empty set of coordinates and count of 0
* Iterate the list and Split based on -> and strip and again split on ,
* If x1 and x2 or y1 and y2 are equal, convert them to int and loop through the not equal value and add to set if not present. If it is already present in set, increment count
'''
from os import path

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        inp = f.read().splitlines()
    return inp

# def closure():
#     count = 0
#     def overlap(x_constant=None, y_constant=None):
#         pass
#     return overlap


def first(vents):
    seen = dict()
    count = 0
    for vent in vents:
        start, end = vent.split('->')
        x1, y1 = map(int, start.strip().split(','))
        x2, y2 = map(int, end.strip().split(','))
        if x1 == x2 or y1 == y2:
            if y1 == y2:
                if x1 < x2:
                    p1 = x1
                    p2 = x2
                else:
                    p1 = x2
                    p2 = x1
                for i in range(p1, p2+1):
                    if (i, y1) in seen.keys():
                        if seen[(i,y1)] == 1:
                            count += 1
                        seen[(i, y1)] += 1
                    else:
                        seen[(i, y1)] = 1
            else:
                if y1 < y2:
                    p1 = y1
                    p2 = y2
                else:
                    p1 = y2
                    p2 = y1
                for i in range(p1, p2+1):
                    if (x1, i) in seen:
                        if seen[(x1, i)] == 1:
                            count += 1
                        seen[(x1, i)] += 1
                    else:
                        seen[(x1, i)]=1
    print(count)

def solve():
    vents = read_input()
    first(vents)
    # second(vents)

solve()
