from asyncore import read
from os import path


def read_input():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        chunk_lines = f.read().splitlines()
    return chunk_lines


def first(chunk_lines):
    closing_braces_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    illegal_closing_braces = {')': 0, ']': 0, '}': 0, '>': 0}
    closing_to_opening_braces = {')': '(', ']': '[', '}': '{', '>': '<'}
    for chunks in chunk_lines:
        stack = []
        for brace in chunks:
            if brace in closing_to_opening_braces:
                if len(stack):
                    opening_brace = stack.pop()
                    if closing_to_opening_braces[brace] == opening_brace:
                        continue
                illegal_closing_braces[brace] += 1
                break
            else:
                stack.append(brace)
    score = 0
    for brace, count in illegal_closing_braces.items():
        score += closing_braces_points[brace] * count
    print(score)

def solution():
    chunk_lines = read_input()
    first(chunk_lines)


solution()
