from utils import read_one


move = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def adjust_tail(prev, curr):
    x_offset = prev[0] - curr[0]
    y_offset = prev[1] - curr[1]
    change = (0, 0)

    if abs(x_offset) >= 2 and abs(y_offset) >= 2:
        change = (
            x_offset - 1 if x_offset > 0 else x_offset + 1,
            y_offset - 1 if y_offset > 0 else y_offset + 1,
        )
    elif abs(x_offset) >= 2:
        change = (x_offset - 1 if x_offset > 0 else x_offset + 1, y_offset)
    elif abs(y_offset) >= 2:
        change = (x_offset, y_offset - 1 if y_offset > 0 else y_offset + 1)

    return (curr[0] + change[0], curr[1] + change[1])


def day09(file, count=2):
    visited = set([f"0:0"])
    knots = [(0, 0)] * count

    for line in read_one(file):
        [dir, count] = line.split(" ")

        for _ in range(int(count)):
            knots[0] = (knots[0][0] + move[dir][0], knots[0][1] + move[dir][1])
            for x in range(1, len(knots)):
                knots[x] = adjust_tail(knots[x - 1], knots[x])
            visited.add(f"{knots[-1][0]}:{knots[-1][1]}")

    return len(visited)


assert day09("test09") == 13
assert day09("test09_2", 10) == 36
print("Part1:\t", day09("input09"))
print("Part2:\t", day09("input09", 10))
