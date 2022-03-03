from os import path

def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        connections = f.read().splitlines()
    adj_list = {}
    for connection in connections:
        src, dest = connection.split('-')
        if src != 'end' and dest != 'start':
            if src in adj_list:
                adj_list[src].append(dest)
            else:
                adj_list[src] = [dest]
        if src != 'start' and dest != 'end':
            if dest in adj_list:
                adj_list[dest].append(src)
            else:
                adj_list[dest] = [src]
    return adj_list

def decision(cave, path_set):
    if cave == 'end' or cave in path_set:
        return False
    return True

def bt(path_set, adj_list, cave):
    count = 0
    # Add
    if cave.islower():
        path_set.add(cave)
    for neighbor in adj_list[cave]:
        # Decide
        if decision(neighbor, path_set):
            count += bt(path_set, adj_list, neighbor)
        if neighbor == 'end':
            count += 1
    # Removal
    if cave.islower():
        path_set.remove(cave)
    return count
        

def first(adj_list):
    path_set = set()
    total = bt(path_set, adj_list, cave='start')
    print(total)


def decision_second(cave, path_set, twice_set):
    if cave == 'end':
        return False
    if cave in path_set:
        if len(twice_set) == 0:
            twice_set.add(cave)
            return True
        return False
    return True

def bt_second(path_set, adj_list, cave, twice_set):
    count = 0
    # Add
    if cave.islower():
        path_set.add(cave)
    for neighbor in adj_list[cave]:
        # Decide
        if decision_second(neighbor, path_set, twice_set):
            count += bt_second(path_set, adj_list, neighbor, twice_set)
        if neighbor == 'end':
            count += 1
    # Removal
    if cave.islower():
        if cave not in twice_set:
            path_set.remove(cave)
        else:
            twice_set.remove(cave)
    return count

def second(adj_list):
    path_set = set()
    twice_set = set()
    total = bt_second(path_set, adj_list, cave='start', twice_set=twice_set)
    print(total)
        

def solution():
    adj_list = read_file()
    # first(adj_list) 
    second(adj_list)
        
solution()