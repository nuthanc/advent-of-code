'''
1. Verify the Constraints
* Only positive integer numbers
* Can the Position that costs the cheapest possible outcome be other than the numbers in the list?
    * Maybe

2. Test Case
* 16,1,2,0,4,2,7,1,2,14

3. Solution without code
* Subproblems
    * Find the number to align to
    * Get the cheapest possible outcome
* I'm finding this similar to Minimum Distance between Source and Destination
* 16 - 16(0)
* 16,1 - 0(16+1=17), 1(15+0=15), 2(14+1=15), 3(13+2=15), 10(6+9=15)
    * For 2 numbers, first_num - second_num
* 16,1,2 - 1(15+0+1=16), 2(14+1+0=15), 3(13+2+1=16), 4(12+3+2=17), 5(11,4,3=18), 6(10+5+4=19), 7(9+6+5=20), 8(8+7+6=21), 9(7+8+7=22), 10(6+9+8=23), 11(5+10+9=24), 12(4+11+10=25), 13(3+12+11=26), 14(2+13+12=27), 15(1+14+13=28), 16(0+15+14=29)
    * 1,2,16 - Diff - (0,1,1=15) (1,0,14)
* 16,1,2,0 - 0(16+1+2+0=19), 1(15+0+1+1=17), 2(14+1+0+2=17), 3(13+2+1+3=19), 4(12+3+2+4=21)
    * 0,1,2,16 - 1,1,14 - 16/4 = 4
* 16,1,2,0,4 - 0(16+1+2+0+4=23), 1(15+0+1+1+3=20), 2(14+1+0+2+2=19), 3(13+2+1+3+1=20), 4(12+3+2+4+0=21)
* 16,1,2,0,12 - 0(16+1+2+0+12=31), 1(15+0+1+1+11=28), 2(14+1+0+2+10=27), 3(13+2+1+3+9=28), 4(12+3+2+4+8=29)
* 1,3,16 - 1(0+2+15=17), 2(1+1+14=16), 3(2+0+13=15);ppplll

Brute force solution of 2 loops, but what about numbers not in list?
'''

from os import path


def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        inp = f.read()
    return [int(pos) for pos in inp.split(',')]

def first(inputs):
    positions = inputs.copy()
    positions.sort()
    # print(positions)
    middle = len(positions) // 2
    opt_position = positions[middle]
    least_fuel = 0
    for position in positions:
        least_fuel += abs(position - opt_position)
    print(least_fuel)

def second(inputs):
    positions = inputs.copy()
    opt_position = round(sum(positions) / len(positions))
    least_fuel = 0
    for position in positions:
        n = abs(position - opt_position)
        least_fuel += ((n * (n+1))/2)
    print(least_fuel)
    

def tester(inputs):
    positions = inputs.copy()
    positions.sort()
    minimum = float('inf')
    opt_pos = float('inf')
    for index in range(positions[-1]+1):
        current_pos = index
        fuel = 0
        for position in positions:
            n = abs(position - current_pos)
            fuel += ((n * (n+1))/2)
        if fuel < minimum:
            minimum = fuel
            opt_pos = current_pos
        # print(f'Fuel for {current_pos} is {fuel}')
    print(f'Optimum fuel of {minimum} at position {opt_pos}')
    print(f'Calculated position: {round(sum(positions) / len(positions))}')
    print(sum(positions))
    print(len(positions))

def solution():
    positions = read_input()
    # first(positions)
    tester(positions)
    # second(positions)  # Getting 489 instead of 488. Pos is 488.507

solution()
