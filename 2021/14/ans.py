from os import path


def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        puzzle_input = f.read()
    polymer_template, pair_insertion = puzzle_input.split('\n\n')
    pair_insertion = pair_insertion.split('\n')
    rules = dict()
    for rule in pair_insertion:
        pair, element = rule.split(' -> ')
        rules[pair] = element
    return polymer_template, rules


def first(polymer_template, rules, steps):
    for _ in range(steps):
        length = len(polymer_template)
        new_template = ''
        for i in range(length-1):
            new_template += polymer_template[i]
            pair = polymer_template[i:i+2]
            element = rules[pair]
            new_template += element
        new_template += polymer_template[-1]
        polymer_template = new_template
    occurence = dict()
    for ele in polymer_template:
        if ele in occurence:
            occurence[ele] += 1
        else:
            occurence[ele] = 1
    print(max(occurence.values()) - min(occurence.values()))


def solution():
    polymer_template, rules = read_file()
    first(polymer_template, rules, 10)


solution()
