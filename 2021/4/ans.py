from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    puzzle_input = f.read()


def get_winning_board_index(boards_element_indices, boards, numbers_drawn, rows_count, cols_count):
    for num in numbers_drawn:
        matrix_len = len(boards[0])
        for i, board_dict in enumerate(boards_element_indices):
            indices = board_dict.get(num)
            if indices:
                board_dict[num][2] = True
                rows_count[i][indices[0]] += 1
                cols_count[i][indices[1]] += 1
                if rows_count[i][indices[0]] == matrix_len:
                    return i, num
                elif cols_count[i][indices[1]] == matrix_len:
                    return i, num


def get_losing_board_score(boards_element_indices, boards, numbers_drawn, rows_count, cols_count):
    board_won = set()
    matrix_len = len(boards[0])
    for num in numbers_drawn:
        for i, board_dict in enumerate(boards_element_indices):
            if i not in board_won:
                indices = board_dict.get(num)
                if indices:
                    board_dict[num][2] = True
                    rows_count[i][indices[0]] += 1
                    cols_count[i][indices[1]] += 1
                    if rows_count[i][indices[0]] == matrix_len:
                        board_won.add(i)
                    elif cols_count[i][indices[1]] == matrix_len:
                        board_won.add(i)
                    if len(board_won) == len(boards):
                        sum = 0
                        for number, indices in board_dict.items():
                            if not indices[2]:
                                sum += int(number)
                        print(sum * int(num))

def first(boards_element_indices, boards,numbers_drawn, rows_count, cols_count):
    index, last_num = get_winning_board_index(boards_element_indices, boards, numbers_drawn, rows_count, cols_count)

    sum = 0
    board_dict = boards_element_indices[index]
    for num, indices in board_dict.items():
        if not indices[2]:
            sum += int(num)
    # print(sum)
    print(sum * int(last_num))
    

def second(boards_element_indices, boards, numbers_drawn, rows_count, cols_count):
    get_losing_board_score(boards_element_indices, boards, numbers_drawn, rows_count, cols_count)


def solution(puzzle_input):
    puzzle_input = puzzle_input.split('\n\n')
    numbers_drawn = puzzle_input[0].split(',')

    # print(numbers_drawn)
    boards = []
    boards_element_indices = []

    for i in range(1, len(puzzle_input)):
        board = []
        board_dict = {}
        for row, content in enumerate(puzzle_input[i].split('\n')):
            elements = content.split()
            for col, ele in enumerate(elements):
                board_dict[ele] = [row, col, False]
            board.append(elements)
        boards.append(board)
        boards_element_indices.append(board_dict)

    rows_count = [[0] * len(boards[0]) for _ in range(len(boards))]
    cols_count = [[0] * len(boards[0]) for _ in range(len(boards))]

    first(boards_element_indices, boards,numbers_drawn, rows_count, cols_count)
    rows_count = [[0] * len(boards[0]) for _ in range(len(boards))]
    cols_count = [[0] * len(boards[0]) for _ in range(len(boards))]
    second(boards_element_indices, boards,numbers_drawn, rows_count, cols_count)
    


solution(puzzle_input)
