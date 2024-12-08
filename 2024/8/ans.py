from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

freq_map = {}


def check_within_bounds(coord):
    x, y = coord
    return x < len(lines) and x >= 0 and y < len(lines[0]) and y >= 0


def first():
    print("FIRST QUESTION")
    distinct_set = set()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch.isalnum():
                if ch in freq_map:
                    freq_map[ch].append((i, j))
                else:
                    freq_map[ch] = [(i, j)]
    for _, values in freq_map.items():
        values.sort(key=lambda k: k[0])
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                first, second = values[i], values[j]
                diff = (second[0] - first[0], second[1] - first[1])
                first_antenna = (first[0] - diff[0], first[1] - diff[1])
                second_antenna = (second[0] + diff[0], second[1] + diff[1])
                if check_within_bounds(first_antenna):
                    distinct_set.add(first_antenna)
                if check_within_bounds(second_antenna):
                    distinct_set.add(second_antenna)
    print(len(distinct_set))


def second():
    print("SECOND QUESTION")
    distinct_set = set()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch.isalnum():
                if ch in freq_map:
                    freq_map[ch].append((i, j))
                else:
                    freq_map[ch] = [(i, j)]

    for _, values in freq_map.items():
        values.sort(key=lambda k: k[0])
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                first, second = values[i], values[j]
                distinct_set.add(first)
                distinct_set.add(second)
                diff = (second[0] - first[0], second[1] - first[1])
                first_antenna = (first[0] - diff[0], first[1] - diff[1])
                second_antenna = (second[0] + diff[0], second[1] + diff[1])
                while check_within_bounds(first_antenna):
                    distinct_set.add(first_antenna)
                    first = first_antenna
                    first_antenna = (first[0] - diff[0], first[1] - diff[1])

                while check_within_bounds(second_antenna):
                    distinct_set.add(second_antenna)
                    second = second_antenna
                    second_antenna = (second[0] + diff[0], second[1] + diff[1])
    print(len(distinct_set))


# first()
second()
