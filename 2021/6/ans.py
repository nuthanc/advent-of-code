'''
Step 1: Verify the Constraints
* Fish after 80 days
* 6 to 0 after which new Fish is spawned with timer 8

Step 2: Write down some Testcases

Step 3: Solution without code
* 3,4,3,1,2
* Iterate from 1 to 80 and iterate through the list and decrement its value
* Check if the decremented value is 0. If yes, append 8 to the list and reset its value to 6
* After the 2 loops, check len of list

Step 4: Solution with code

Step 5: Double check for errors

Step 6: Walk through the Test case

Step 7: Time and Space Complexity

3,4,3,1,2

4,5,4,2,3
7,7,7,7,7
'''
from os import path

def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        inp = f.read()
    return inp

def first(fish_timer, days):
    for day in range(days):
        length = len(fish_timer)
        for i in range(length):
            if fish_timer[i] == 0:
                fish_timer.append(8)
                fish_timer[i] = 7
            fish_timer[i] -= 1
    print(len(fish_timer))
    
def spawn_cycle(rem_days, dp):
    if rem_days < 0:
        return 0
    elif dp.get(rem_days):
        return dp.get(rem_days)
    else:
        dp[rem_days] = 1 + spawn_cycle(rem_days-7, dp) + spawn_cycle(rem_days-9, dp)
        return dp[rem_days]
    
def second(fish_timer, days):
    total = 0
    dp = {}
    for timer in fish_timer:
        rem_days = days - (timer + 1)
        if rem_days >= 0:
            total += 1 + spawn_cycle(rem_days-7, dp) + spawn_cycle(rem_days-9, dp)
    print(total + len(fish_timer))

def solution():
    inp = read_input()
    fish_timer = [int(timer) for timer in inp.split(',')]
    days = 80
    first(fish_timer.copy(), days)
    days = 256
    second(fish_timer, days)

solution()
