from os import path
from functools import cmp_to_key
from collections import Counter

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

card_strength = {
    'A': 5,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 1
}

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
    n = len(first_hand_counter_values)
    m = len(first_hand_counter_values)

    if first_hand_counter_values[-1] == second_hand_counter_values[-1]:
        # First Counter values Comparison
        index_first, index_second = n - 2, m - 2
        while index_first >= 0 and index_second >= 0 and first_hand_counter_values[index_second] == second_hand_counter_values[index_second]:
            index_first -= 1
            index_second -= 1
        if index_first >= 0 and index_second >= 0:
            return first_hand_counter_values[index_first] - second_hand_counter_values[index_second]
        elif index_first >= 0:
            return -1
        elif index_second >= 0:
            return 1
        # Next Hand Lexicographic Comparison
        # Need to handle for 'A' > 'Q' and other character cases
        for i in range(len(first_hand)):
            first_hand_ch, second_hand_ch = first_hand[i], second_hand[i]
            if first_hand_ch == second_hand_ch:
                continue
            if first_hand_ch.isalpha() and second_hand_ch.isalpha():
                return card_strength[first_hand_ch] - card_strength[second_hand_ch]
            else:
                return ord(first_hand_ch) - ord(second_hand_ch)
    else:
        return first_hand_counter_values[-1] - second_hand_counter_values[-1]
    

def first():
    sorted_hand_bids = sorted(hand_bids, key=cmp_to_key(comparator))
    s = 0
    for i in range(len(sorted_hand_bids)):
        _, bid = sorted_hand_bids[i]
        s += (i+1) * bid
    print(s)

def second():
    pass


first()
