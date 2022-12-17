from utils import read_many, read_one
import json
from operator import mul
from functools import reduce, cmp_to_key


def is_ordered(left, right):
    l_is_list = type(left) is list
    r_is_list = type(right) is list
    if not l_is_list and not r_is_list:
        return left - right
    if l_is_list and not r_is_list:
        return is_ordered(left, [right])
    if not l_is_list and r_is_list:
        return is_ordered([left], right)
    if l_is_list and r_is_list:
        i = 0
        while i < len(left) and i < len(right):
            result = is_ordered(left[i], right[i])
            if result != 0:
                return result
            i += 1
        return len(left) - len(right)


def day13_1(file: str):
    result = 0
    for i, [left, right, _] in enumerate(read_many(file, 3)):
        if is_ordered(json.loads(left), json.loads(right)) < 0:
            result += i + 1
    return result


def day13_2(file: str):
    dividers = [[[2]], [[6]]]
    rec_packets = [json.loads(p) for p in read_one(file) if len(p) > 0]
    all_packets = [*rec_packets, *dividers]
    s_packets = sorted(all_packets, key=cmp_to_key(lambda x, y: is_ordered(x, y)))
    return reduce(mul, [i + 1 for i, x in enumerate(s_packets) if x in dividers], 1)


assert day13_1("test13") == 13
assert day13_2("test13") == 140
print("Part1:\t", day13_1("input13"))
print("Part2:\t", day13_2("input13"))
