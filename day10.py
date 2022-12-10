from utils import read_one


def get_operation(line):
    return (1, 0) if line == "noop" else (2, int(line.split(" ")[1]))


def day10(file):
    cycle = 0
    x = 1
    counter = 0
    next_c = 20
    for line in read_one(file):
        cycle_change, diff = get_operation(line)
        cycle += cycle_change
        if cycle >= next_c:
            counter += next_c * x
            next_c += 40
        x += int(diff)
    return counter


def day10_2(file):
    cycle = 0
    x = 1
    sb = ""
    for line in read_one(file):
        cycle_change, diff = get_operation(line)
        for i in range(cycle_change):
            sb += "." if abs(((cycle + i) % 40) - x) > 1 else "#"
            if (cycle + i + 1) % 40 == 0:
                sb += "\n"
        cycle += cycle_change
        x += int(diff)
    return sb.strip()


assert day10("test10") == 13140
assert day10_2("test10") == (
    "##..##..##..##..##..##..##..##..##..##..\n"
    "###...###...###...###...###...###...###.\n"
    "####....####....####....####....####....\n"
    "#####.....#####.....#####.....#####.....\n"
    "######......######......######......####\n"
    "#######.......#######.......#######....."
)

print("Part1:\t", day10("input10"))
print(f"Part2:\n{day10_2('input10')}")
