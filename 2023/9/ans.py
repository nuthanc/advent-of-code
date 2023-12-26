from os import path

THIS_DIR = path.dirname(__file__)
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    lines = f.read().splitlines()

report = [list(map(int, line.split())) for line in lines]

def first():
    history_sum = 0
    for entry in report:
        line_histories, next_seq, count, line = [entry[-1]], [], 0, entry.copy()
        while len(line) and count != len(line):
            count = 0
            for i in range(1, len(line)):
                diff = line[i] - line[i-1]
                if diff == 0:
                    count += 1
                next_seq.append(diff)
            line = next_seq
            line_histories.append(line[-1])
            next_seq = []
        history = 0
        for i in range(len(line_histories)-1, -1, -1):
            history += line_histories[i]
        history_sum += history
    print(history_sum)


def second():
    history_sum = 0
    for entry in report:
        line_histories, next_seq, count, line = [
            entry[0]], [], 0, entry.copy()
        while len(line) and count != len(line):
            count = 0
            for i in range(1, len(line)):
                diff = line[i] - line[i-1]
                if diff == 0:
                    count += 1
                next_seq.append(diff)
            line = next_seq
            line_histories.append(line[0])
            next_seq = []
        history = 0
        for i in range(len(line_histories)-2, -1, -1):
            history = line_histories[i] - history
        history_sum += history
    print(history_sum)


second()
