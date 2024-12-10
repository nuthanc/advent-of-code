from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    input_string = f.read()


def first():
    id = 0
    parsed_list = []
    for i in range(0, len(input_string), 2):
        file_block = int(input_string[i])
        free_space = int(input_string[i + 1]) if i + 1 < len(input_string) else None
        for _ in range(file_block):
            parsed_list.append(id)
        if free_space:
            for _ in range(free_space):  # Free Space = -1
                parsed_list.append(-1)
        id += 1

    non_space_index = None
    for i in range(len(parsed_list) - 1, -1, -1):
        if parsed_list[i] != -1:
            non_space_index = i
            break

    for i in range(len(parsed_list)):
        if parsed_list[i] == -1 and non_space_index > i:
            parsed_list[i] = parsed_list[non_space_index]
            parsed_list[non_space_index] = -1
            non_space_index -= 1
            while parsed_list[non_space_index] == -1:
                non_space_index -= 1

    s = 0
    for i, id in enumerate(parsed_list):
        if id != -1:
            s += i * id
    print(s)


def second():
    id = 0
    parsed_list = []
    file_blocks = []  # (block_size, start_index, id)
    free_spaces = []  # (space_size, start_index)
    for i in range(0, len(input_string), 2):
        file_block = int(input_string[i])
        file_blocks.append((file_block, len(parsed_list), id))
        free_space = int(input_string[i + 1]) if i + 1 < len(input_string) else None
        for _ in range(file_block):
            parsed_list.append(id)
        if free_space:
            free_spaces.append((free_space, len(parsed_list)))
            for _ in range(free_space):  # Free Space = -1
                parsed_list.append(-1)
        id += 1

    # print("".join([str(x) for x in parsed_list]))
    # print(file_blocks)
    # print(free_spaces)
    for i in range(len(file_blocks) - 1, -1, -1):
        for j in range(len(free_spaces)):
            space_size, space_start_index = free_spaces[j]
            block_size, file_start_index, file_id = file_blocks[i]
            if space_size >= block_size and file_start_index > space_start_index:
                for k in range(space_start_index, space_start_index + block_size):
                    parsed_list[k] = file_id
                for k in range(file_start_index, file_start_index + block_size):
                    parsed_list[k] = -1
                free_spaces[j] = (
                    space_size - block_size,
                    space_start_index + block_size,
                )
                break
    # print("".join([str(x) for x in parsed_list]))
    s = 0
    for i, id in enumerate(parsed_list):
        if id != -1:
            s += i * id
    print(s)


# first()
second()
