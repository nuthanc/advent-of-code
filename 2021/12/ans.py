from os import path

def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        connections = f.read().splitlines()
    adj_list = {}
    for connection in connections:
        src, dest = connection.split('-')
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
    # if cave == 'end' or (cave.islower() and cave in paths):
    if cave == 'end' or cave in path_set:
        return False
    return True

# def bt(paths, adj_list, cave):
def bt(path_set, adj_list, cave):
    count = 0
    # Add
    # paths.append(cave)
    if cave.islower():
        path_set.add(cave)
    for neighbor in adj_list[cave]:
        # Decide
        # if decision(neighbor, paths):
        #     count += bt(paths, adj_list, neighbor)
        if decision(neighbor, path_set):
            count += bt(path_set, adj_list, neighbor)
        if neighbor == 'end':
            count += 1
    # Removal
    # paths.pop()
    if cave.islower():
        path_set.remove(cave)
    return count
        

def first(adj_list):
    # paths = []
    # total = bt(paths, adj_list, cave='start')
    path_set = set()
    total = bt(path_set, adj_list, cave='start')
    print(total)
        

def solution():
    adj_list = read_file()
    print(adj_list)
    first(adj_list)    
        
solution()