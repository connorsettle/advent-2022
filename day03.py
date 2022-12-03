from utils import read_one, read_many


def get_num_val(char):
    val = ord(char)
    if val >= 97:
        return val - 96
    return val - 38


def day03_p1(file):
    counter = 0
    for line in read_one(file):
        half = int(len(line) / 2)
        first_comp = set([*line[:half]])
        second_comp = set([*line[half:]])
        common_var = [*first_comp.intersection(second_comp)][0]
        counter += get_num_val(common_var)
    return counter


def day03_p2(file):
    counter = 0
    for lines in read_many(file, 3):
        [first, *other] = [set([*line]) for line in lines]
        common_var = [*first.intersection(*other)][0]
        counter += get_num_val(common_var)
    return counter


assert day03_p1("test03") == 157
assert day03_p2("test03") == 70
print("Part1:\t", day03_p1("input03"))
print("Part2:\t", day03_p2("input03"))
