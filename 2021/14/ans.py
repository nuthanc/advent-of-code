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


def second(polymer_template, rules, steps):
    pair_count = {}
    for first, second in zip(polymer_template, polymer_template[1:]):
        pair = first + second
        if pair not in pair_count:
            pair_count[pair] = 0
        pair_count[pair] += 1
    for _ in range(steps):
        new_dict = {}
        for pair in pair_count:
            ele = rules[pair]
            new_pair = pair[0] + ele
            if new_pair not in new_dict:
                new_dict[new_pair] = pair_count[pair]
            else:
                new_dict[new_pair] += pair_count[pair]
            new_pair = ele + pair[1]
            if new_pair not in new_dict:
                new_dict[new_pair] = pair_count[pair]
            else:
                new_dict[new_pair] += pair_count[pair]
        pair_count = new_dict
    first_count, second_count = {}, {}
    for pair in pair_count:
        first, second = pair
        if first not in first_count:
            first_count[first] = pair_count[pair]
        else:
            first_count[first] += pair_count[pair]
        if second not in second_count:
            second_count[second] = pair_count[pair]
        else:
            second_count[second] += pair_count[pair]
    final_dict = {k: max(first_count.get(k,0), second_count.get(k,0)) for k in (first_count.keys() | second_count.keys())}
    print(max(final_dict.values()) - min(final_dict.values()))


def solution():
    polymer_template, rules = read_file()
    # first(polymer_template, rules, 10)
    second(polymer_template, rules, 40)


solution()
