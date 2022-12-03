from utils import read_one


def get_num(val):
    if val == "A" or val == "X":
        return 0
    if val == "B" or val == "Y":
        return 1
    if val == "C" or val == "Z":
        return 2


def parser_vals(line):
    [oppStr, myStr] = line.split(" ")
    return (get_num(oppStr), get_num(myStr))


def day02_p1(file):
    counter = 0
    for line in read_one(file):
        (opp, my) = parser_vals(line)
        counter += my + 1
        if opp == my:
            counter += 3
        elif (opp + 1) % 3 == my:
            counter += 6
    return counter


def day02_p2(file):
    counter = 0
    for line in read_one(file):
        (opp, my) = parser_vals(line)
        counter += 1 + my * 3 + (opp + my + 2) % 3
    return counter


assert day02_p1("test02") == 15
assert day02_p2("test02") == 12
print("Part1:\t", day02_p1("input02"))
print("Part2:\t", day02_p2("input02"))
