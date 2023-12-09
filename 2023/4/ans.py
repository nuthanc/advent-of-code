from os import path
from re import findall

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    cards = f.read().splitlines()

def first():
    s = 0
    for card in cards:
        _, numbers = card.split(':')
        winning, current = numbers.split('|')
        winning_numbers = findall('\d+', winning)
        current_numbers = findall('\d+', current)
        winning_numbers_set = set(winning_numbers)
        current_numbers_set = set(current_numbers)
        matches = len(winning_numbers_set.intersection(current_numbers_set))
        s += 2**(matches - 1) if matches >= 1 else 0
    print(s)


def second():
    s = 0
    cards_count = {}
    for i in range(len(cards)):
        cards_count[i] = 1

    for index, card in enumerate(cards):
        _, numbers = card.split(':')
        winning, current = numbers.split('|')
        winning_numbers = findall('\d+', winning)
        current_numbers = findall('\d+', current)
        winning_numbers_set = set(winning_numbers)
        current_numbers_set = set(current_numbers)
        matches = len(winning_numbers_set.intersection(current_numbers_set))
        
        for i in range(index+1, index+1+matches):
            if i < len(cards):
                cards_count[i] += 1 * cards_count[index]
            else:
                break

    for card_num in cards_count:
        s += cards_count[card_num]
    # print(cards_count)
    print(s)


second()
