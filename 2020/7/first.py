# Day 7: Handy Haversacks: https://adventofcode.com/2020/day/7
import re
from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    bag_list = f.read().splitlines()

max = 0
for line in bag_list:
    bag_string, content = line.split("contain")
    content_list = re.findall(r'(\d)([\w\s]+)bag.', content)
    contrast, color, _ = bag_string.split("bags")[0].split(" ")
    bag = f'{contrast}_{color}'
    print(bag)
    print(content_list)

