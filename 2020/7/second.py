# Day 7: Handy Haversacks: https://adventofcode.com/2020/day/7#part2
import re
from os import path

THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    bag_list = f.read().splitlines()

bag_dict = {}

for line in bag_list:
    container_bags, content = line.split("contain")
    content_list = re.findall(r'(\d)([\w\s]+)bag.', content)
    container_color = container_bags.split("bags")[0].strip()
    contained_bags = [(num, bag.strip()) for num, bag in content_list]
    bag_dict[container_color] = contained_bags

# for k,v in bag_dict.items():
#     print(k,v)

# shiny gold  [('5', 'light black'), ('3', 'mirrored yellow'), ('5', 'muted plum')]

# 1: Recursion
# Check this for recursion in for loop: https://stackoverflow.com/questions/4795527/how-recursion-works-inside-a-for-loop#:~:text=Just%20because%20the%20function%20happens,functions%20again%2C%20and%20so%20on.&text=For%20recursion%2C%20it's%20helpful%20to,stack%20structure%20in%20your%20mind.
# My earlier solution doesn't consider the container bags, it only considers the contained bags

def find_bags(bags):
    if len(bags) == 0:
        return 1

    part_sum = 0
    for num, bag in bags:
        n = int(num)
        val = find_bags(bag_dict[bag]) # By separating into this, I was able to get the answer
        if val != 1:
            part_sum += n + n * val 
        else:
            # Initially was part_sum += n *find_bags(bag_dict[bag])
            part_sum += n * val
        # print(bag, n, part_sum)

    return part_sum # Return must be some value

# print(bag_dict['shiny gold'])

print(find_bags(bag_dict['shiny gold']))
