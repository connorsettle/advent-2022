from utils import read_one
from functools import reduce


def add_char(acc, char):
    if not char in acc:
        acc[char] = 1
    else:
        acc[char] += 1
    return acc


def remove_char(acc, char):
    if acc[char] == 1:
        del acc[char]
    else:
        acc[char] -= 1
    return acc


def day06(file, n):
    line = next(read_one(file))
    n_chars = reduce(add_char, line[:n], {})
    for i in range(n, len(line)):
        if line[i] != line[i - n]:
            add_char(n_chars, line[i])
            remove_char(n_chars, line[i - n])
        if len(n_chars) == n:
            return i + 1
    return -1


assert day06("test06", 4) == 7
assert day06("test06", 14) == 19
print("Part1:\t", day06("input06", 4))
print("Part2:\t", day06("input06", 14))
