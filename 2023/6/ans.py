from os import path
from re import findall

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

time_str = findall('\d+', lines[0])
dist_str = findall('\d+', lines[1])

time_list = [int(x) for x in time_str]
dist_list = [int(x) for x in dist_str]

'''
Time(equivalent to Speed since 1ms -> 1 mm/ms) * Remaining Time

t -> Range from 0 to given time(gt)
Condition: t * (gt - t) > dist

'''


def first():
    ans = 1
    for i, given_time in enumerate(time_list):
        ways = 0
        for time in range(1, given_time):
            if time * (given_time - time) > dist_list[i]:
                ways += 1
        ans *= ways

    print(ans)

# Try to optimize this later
def second():
    given_time = int(''.join(time_str))
    dist = int(''.join(dist_str))
    ways = 0
    for time in range(1, given_time):
        if time * (given_time - time) > dist:
            ways += 1
    print(ways)

second()
