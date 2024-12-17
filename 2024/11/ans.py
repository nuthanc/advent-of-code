from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    line = f.read()

BLINK_TIMES = 25

def first():
    stone_list = line.split(' ')
    for i in range(BLINK_TIMES):
        new_list = []
        for stone in stone_list:
            if stone == '0':
                new_list.append('1')
            elif len(stone) % 2 == 0:
                first_half = stone[:len(stone)//2]
                second_half = str(int(stone[len(stone)//2:]))
                new_list.append(first_half)
                new_list.append(second_half)
            else:
                new_list.append(str(int(stone) * 2024))
        stone_list = new_list
    print(len(stone_list))

def second():
    stone_list = line.split(" ")
    for i in range(75):
        new_list = []
        for stone in stone_list:
            if stone == "0":
                new_list.append("1")
            elif len(stone) % 2 == 0:
                first_half = stone[: len(stone) // 2]
                second_half = str(int(stone[len(stone) // 2 :]))
                new_list.append(first_half)
                new_list.append(second_half)
            else:
                new_list.append(str(int(stone) * 2024))
        stone_list = new_list
    print(len(stone_list))


first()
# second()
