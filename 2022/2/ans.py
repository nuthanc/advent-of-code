from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors
mapping = {"A": "X", "B": "Y", "C": "Z"}


def get_points(opp, you):
    # Draw case
    if mapping[opp] == you:
        return 3
    # Win case
    if (
        (opp == "A" and you == "Y")
        or (opp == "B" and you == "Z")
        or (opp == "C" and you == "X")
    ):
        return 6
    return 0


shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def first():
    score = 0
    for line in lines:
        opp, you = line.split()
        score += shape_score[you] + get_points(opp, you)
    print(score)


def get_points_second(result):
    # X - loss, Y - draw, Z - win
    if result == "X":
        return 0
    if result == "Y":
        return 3
    return 6


win_map = {"A": "B", "B": "C", "C": "A"}
loss_map = {"B": "A", "C": "B", "A": "C"}


# A - Rock
# B - Paper
# C - Scissors
def get_shape_score(opp, result):
    # Draw
    if result == "Y":
        return shape_score[mapping[opp]]
    # Win
    if result == "Z":
        return shape_score[mapping[win_map[opp]]]
    return shape_score[mapping[loss_map[opp]]]


def second():
    score = 0
    for line in lines:
        opp, result = line.split()
        score += get_shape_score(opp, result) + get_points_second(result)
    print(score)


# first()
second()
