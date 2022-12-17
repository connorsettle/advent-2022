from utils import read_one
from typing import Tuple, Set, List


def get_val(val):
    match val:
        case "E":
            return 26
        case "S":
            return 1
        case _:
            return ord(val) - 96


def nodeToKey(pos: Tuple[int, int]) -> str:
    return f"{pos[0]}:{pos[1]}"


def keyToNode(val: str) -> Tuple[int, int]:
    [x, y] = val.split(":")
    return (int(x), int(y))


def get_next_steps(
    positions: Set[str], unvisited: Set[str], state: List[List[int]]
) -> Set[str]:
    next_steps = set()
    for curr in positions:
        x, y = keyToNode(curr)
        for pos in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            key = nodeToKey(pos)
            if (
                0 <= pos[0] < len(state[0])
                and 0 <= pos[1] < len(state)
                and key in unvisited
            ):
                if state[y][x] + 1 >= state[pos[1]][pos[0]]:
                    next_steps.add(key)
                    unvisited.remove(key)
    return next_steps


def get_coords_by_val(state: List[List[str]], values: List[str]):
    result = []
    for y, row in enumerate(state):
        for x, val in enumerate(row):
            if val in values:
                result.append(nodeToKey((x, y)))
    return result


def day12(file: str, start_vals: List[str]):
    state_str = [list(line) for line in read_one(file)]
    start = get_coords_by_val(state_str, start_vals)
    target = get_coords_by_val(state_str, ["E"])[0]

    state = [[get_val(val) for val in row] for row in state_str]
    unvisited = set()
    for y, row in enumerate(state):
        unvisited.update([nodeToKey((x, y)) for x, _ in enumerate(row)])
    positions = set(start)
    unvisited = unvisited.difference(positions)

    steps = 0
    while target not in positions:
        positions = get_next_steps(positions, unvisited, state)
        steps += 1

    return steps


assert day12("test12", ["S"]) == 31
assert day12("test12", ["S", "a"]) == 29
print("Part1:\t", day12("input12", ["S"]))
print("Part2:\t", day12("input12", ["S", "a"]))
