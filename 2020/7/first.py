# Day 7: Handy Haversacks: https://adventofcode.com/2020/day/7
import re
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    bag_list = f.read().splitlines()

bag_dict = {}
direct_container_bags = []
req_bag = 'shiny gold'
parent_bag_dict = {}

for line in bag_list:
    container_bags, content = line.split("contain")
    content_list = re.findall(r'(\d)([\w\s]+)bag.', content)
    contrast, color, _ = container_bags.split("bags")[0].split(" ")
    container_color = f'{contrast} {color}'
    # print(container_bags)
    # print(content_list)
    contained_bags = [bag.strip() for num, bag in content_list]
    bag_dict[container_color] = contained_bags

    for bag in contained_bags:
        if req_bag == bag:
            direct_container_bags.append(container_color)
        if parent_bag_dict.get(bag):
            parent_bag_dict[bag].append(container_color)
        else:
            parent_bag_dict[bag] = [container_color]



# for k, v in bag_dict.items():
#     print(f'{k}: {v}')
for k,v in parent_bag_dict.items():
    print(f'{k}: {v}')
print(direct_container_bags)

uniq_set = set()


def recursively_add_to_set(bag):
    if bag in uniq_set:
        return
    else:
        uniq_set.add(bag)
        if parent_bag_dict.get(bag) is not None:
            for b in parent_bag_dict[bag]:
                recursively_add_to_set(b)

for bag in direct_container_bags:
    recursively_add_to_set(bag)

    
print(uniq_set)
print(len(uniq_set))
