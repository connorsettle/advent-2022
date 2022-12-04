from utils import read_one


def parse_line(line):
    all_elf_min_max = [elf_range.split("-") for elf_range in line.split(",")]
    return [
        (int(elf_min_max[0]), int(elf_min_max[1])) for elf_min_max in all_elf_min_max
    ]


def is_fully_contained(range1, range2):
    return range1[0] >= range2[0] and range1[1] <= range2[1]


def day04_p1(file):
    counter = 0
    for line in read_one(file):
        [range1, range2] = parse_line(line)
        if is_fully_contained(range1, range2) or is_fully_contained(range2, range1):
            counter += 1
    return counter


def day04_p2(file):
    counter = 0
    for line in read_one(file):
        [range1, range2] = parse_line(line)
        if range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]:
            counter += 1
        elif is_fully_contained(range2, range1):
            counter += 1
    return counter


assert day04_p1("test04") == 2
assert day04_p2("test04") == 4
print("Part1:\t", day04_p1("input04"))
print("Part2:\t", day04_p2("input04"))
