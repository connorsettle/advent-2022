from utils import read_one


def parse_state(lines):
    state = []
    moves = []
    for l in lines:
        if l.startswith("move"):
            [_, count, _, source, _, destination] = l.split(" ")
            moves.append((int(count), int(source) - 1, int(destination) - 1))
        elif len(l) > 0:
            row = 0
            i = 0
            while i < len(l):
                if len(state) < row + 1:
                    state += [[]] * (row + 1 - len(state))
                if l[i] == "[":
                    state[row].append(l[i + 1 : i + 2])
                row += 1
                i = row * 4
    for s in state:
        s.reverse()
    return (state, moves)


def day05_p1(file):
    (state, moves) = parse_state(read_one(file, False))
    for (count, source, destination) in moves:
        for _ in range(0, count):
            state[destination].append(state[source].pop())
    return "".join([x.pop() if len(x) > 0 else " " for x in state])


def day05_p2(file):
    (state, moves) = parse_state(read_one(file, False))
    for (count, source, destination) in moves:
        after_move, to_move = (
            state[source][: len(state[source]) - count],
            state[source][len(state[source]) - count : len(state[source])],
        )
        state[source] = after_move
        state[destination] += to_move
    return "".join([x.pop() if len(x) > 0 else " " for x in state])


assert day05_p1("test05") == "CMZ"
assert day05_p2("test05") == "MCD"
print("Part1:\t", day05_p1("input05"))
print("Part2:\t", day05_p2("input05"))
