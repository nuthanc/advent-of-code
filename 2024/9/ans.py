from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    input_string = f.read()


def first():
    id = 0
    parsed_list = [] # Change this to list later
    for i in range(0, len(input_string), 2):
        file_block = int(input_string[i])
        free_space = int(input_string[i+1]) if i+1 < len(input_string) else None
        for _ in range(file_block):
            parsed_list.append(id)
        if free_space:
            for _ in range(free_space): # Free Space = -1
                parsed_list.append(-1)
        id += 1

    i = 0
    while i < len(parsed_list):
        if parsed_list[i] == -1:
            popped = parsed_list.pop()
            while popped == -1:
                popped = parsed_list.pop()
            parsed_list[i] = popped
        i += 1

    s = 0
    for i, item in enumerate(parsed_list):
        s += i * item
    print(s)

def second():
    pass


first()
