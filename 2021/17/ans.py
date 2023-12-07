'''
Step 1: Verify the Constraints
    * velocity in x(forward, so always +ve) and y(upward or downward if negative) directions
        * i.e 1st value in velocity in x direction and 2nd value is velocity in y direction
    * Starting position of probe 0,0 position
    * After **any** step, it should be within the target area(Equal to and in between)
    * On each step
        * The probe's x position increases by its vx velocity and drag effect
            * if vx > 0, vx-=1 and (x+vx) else if vx=0, vx=0 else vx+=1 and (x+vx)
        * The probe's y position increases by its vy velocity
            * vy-=1 and (y+vy)
Step 2: Write down some test cases

Step 3: Solution without code
    * Use formula like for 5th term Iv + (Iv-5) + ....(Iv-1)
    * Then maybe use binary search technique to decrement or increment
    * For a Iv, there is a max limit and min limit in x direction   
        * Max limit is Iv(Iv+1)/2 and min limit is Iv -> Same for y direction for positive
'''

from os import path
import re

def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        return f.read()


inp = read_file()
minx, maxx, miny, maxy = map(int, re.findall(r"-?\d+", inp))


def steps_for_dy(dy):
    y = 0
    steps = 0
    valid = []
    print(dy)
    while y >= miny:
        if miny <= y <= maxy:
            valid.append(steps)
        y += dy
        dy -= 1
        steps += 1
    print(valid)
    return valid


def can_land_dx(step):
    for dx in range(1, maxx):
        x = 0
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
        if minx <= x <= maxx:
            return True
    return False


dy = -miny

while True:
    if any(can_land_dx(step) for step in steps_for_dy(dy)):
        print(sum(range(1, dy + 1)))
        break
    dy -= 1
