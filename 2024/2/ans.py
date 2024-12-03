from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, "input.txt")
with open(file_path) as f:
    lines = f.read().splitlines()

reports = []
for line in lines:
    reports.append([int(x) for x in line.split(" ")])


def check_increasing(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if report[i] <= report[i - 1] or (diff <= 0 or diff > 3):
            return False
    return True


def check_decreasing(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if report[i] >= report[i - 1] or (diff <= 0 or diff > 3):
            return False
    return True


def check_increasing_second(report):
    count = 0
    i = 1
    while i < len(report):
        diff = abs(report[i] - report[i - 1])
        if report[i] <= report[i - 1] or (diff <= 0 or diff > 3):
            if count == 0:
                count += 1
                delete_i = i + 1 >= len(report) or (
                    report[i - 1] < report[i + 1]
                    and (0 < (report[i + 1] - report[i - 1]) <= 3)
                )
                delete_i_minus_1 = i - 2 < 0 or (
                    report[i - 2] < report[i] and (0 < (report[i] - report[i - 2]) <= 3)
                )
                if not delete_i and not delete_i_minus_1:
                    return False
                if delete_i:
                    i += 2
                    continue
                if delete_i_minus_1:
                    i += 1
                    continue
            else:
                return False
        i += 1
    return True


def check_decreasing_second(report):
    count = 0
    i = 1
    while i < len(report):
        diff = abs(report[i] - report[i - 1])
        if report[i] >= report[i - 1] or (diff <= 0 or diff > 3):
            if count == 0:
                count += 1
                delete_i = i + 1 >= len(report) or (
                    report[i - 1] > report[i + 1]
                    and (0 < (report[i - 1] - report[i + 1]) <= 3)
                )
                delete_i_minus_1 = i - 2 < 0 or (
                    report[i - 2] > report[i] and (0 < (report[i - 2] - report[i]) <= 3)
                )
                if not delete_i and not delete_i_minus_1:
                    return False
                if delete_i:
                    i += 2
                    continue
                if delete_i_minus_1:
                    i += 1
                    continue
            else:
                return False
        i += 1
    return True


def first():
    print("FIRST QUESTION")
    count = 0
    for report in reports:
        increasing = check_increasing(report)
        decreasing = check_decreasing(report)
        if increasing or decreasing:
            count += 1
    print(count)


def second():
    print("SECOND QUESTION")
    count = 0
    for report in reports:
        increasing = check_increasing_second(report)
        decreasing = check_decreasing_second(report)
        if increasing or decreasing:
            count += 1
    print(count)


first()
# second()
