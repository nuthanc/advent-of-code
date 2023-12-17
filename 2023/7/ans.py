from os import path
from functools import cmp_to_key
from collections import Counter

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

hand_bids = []
for line in lines:
    hand, bid_str = line.split()
    hand_bids.append((hand, int(bid_str)))

def comparator(a, b):
    first_hand, second_hand = a[0], b[0]
    first_hand_counter = Counter(first_hand)
    second_hand_counter = Counter(second_hand)
    first_hand_counter_values = sorted(first_hand_counter.values())
    second_hand_counter_values = sorted(second_hand_counter.values())

    if first_hand_counter_values[-1] == second_hand_counter_values[-1]:
        # First Counter values Comparison
        ind = len(first_hand_counter_values) - 2
        while ind >= 0 and first_hand_counter_values[ind] == second_hand_counter_values[ind]:
            ind -= 1
        if ind >= 0:
            return first_hand_counter_values[ind] - second_hand_counter_values[ind]
        # Next Hand Lexicographic Comparison
        # Need to handle for 'A' > 'Q' and other character cases
        if first_hand < second_hand:
            return -1
        else:
            return 1
    else:
        return first_hand_counter_values[-1] - second_hand_counter_values[-1]
    

def first():
    sorted_hand_bids = sorted(hand_bids, key=cmp_to_key(comparator))
    print('sorted_hand_bids', sorted_hand_bids)


def second():
    pass


first()
