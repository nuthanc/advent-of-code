from os import path
from re import findall

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read()

data = lines.split('\n\n')
# print(data)
seeds = data[0].split(':')[1].strip().split()


def first():
    seed_map = {}
    for seed in seeds:
        seed_map[seed] = seed

    for i in range(1, len(data)):
        mappings_string = data[i]
        values = mappings_string.split('\n')[1:]
        for seed in seed_map:
            seed_val = int(seed_map[seed])
            for line in values:
                dst_start_range_str, src_start_range_str, range_len_str = findall(
                    '\d+', line)
                dst_start_range, src_start_range, range_len = int(dst_start_range_str), int(
                    src_start_range_str), int(range_len_str)
                if seed_val >= src_start_range and seed_val < src_start_range + range_len:
                    seed_map[seed] = str((
                        seed_val - src_start_range) + dst_start_range)
                    break
    locations = [int(x) for x in seed_map.values()]
    print(min(locations))

def second():
    seed_map = {}
    for i in range(0, len(seeds), 2):
        start, start_range = int(seeds[i]), int(seeds[i+1])
        for j in range(start, start + start_range):
            seed = j
            seed_map[seed] = str(seed)

    for i in range(1, len(data)):
        mappings_string = data[i]
        values = mappings_string.split('\n')[1:]
        for seed in seed_map:
            seed_val = int(seed_map[seed])
            for line in values:
                dst_start_range_str, src_start_range_str, range_len_str = findall(
                    '\d+', line)
                dst_start_range, src_start_range, range_len = int(dst_start_range_str), int(
                    src_start_range_str), int(range_len_str)
                if seed_val >= src_start_range and seed_val < src_start_range + range_len:
                    seed_map[seed] = str((
                        seed_val - src_start_range) + dst_start_range)
                    break
    locations = [int(x) for x in seed_map.values()]
    print(min(locations))


def second_with_bs():
    # Only start and enda
    seed_map = {}
    for i in range(0, len(seeds), 2):
        start, start_range = int(seeds[i]), int(seeds[i+1])
        for j in range(start, start + start_range):
            seed = j
            seed_map[seed] = str(seed)
    print(seed_map)

    # for i in range(1, len(data)):
    #     mappings_string = data[i]
    #     values = mappings_string.split('\n')[1:]
    #     for seed in seed_map:
    #         seed_val = int(seed_map[seed])
    #         for line in values:
    #             dst_start_range_str, src_start_range_str, range_len_str = findall(
    #                 '\d+', line)
    #             dst_start_range, src_start_range, range_len = int(dst_start_range_str), int(
    #                 src_start_range_str), int(range_len_str)
    #             if seed_val >= src_start_range and seed_val < src_start_range + range_len:
    #                 seed_map[seed] = str((
    #                     seed_val - src_start_range) + dst_start_range)
    #                 break
    # locations = [int(x) for x in seed_map.values()]
    # print(min(locations))

# second()
second_with_bs()
