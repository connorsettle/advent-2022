import re

from dataclasses import dataclass, field
from functools import reduce
from math import lcm
from operator import mul
from typing import List, Tuple
from utils import read_one


@dataclass
class Monkey:
    id: int
    items: List[int] = field(default_factory=list)
    op_args: List[int | str] = field(default_factory=list)
    op_func = ""
    test_mod = 0
    test_on_failure = 0
    test_on_success = 0
    totals_inspects = 0

    def process(
        self, prev_worry: int, relief: bool, least_common_mult: int
    ) -> Tuple[int, int]:
        self.totals_inspects += 1
        args = [prev_worry if x == "old" else x for x in self.op_args]
        worry = reduce(mul, args, 1) if self.op_func == "*" else sum(args)

        if relief:
            worry = int(worry / 3)
        worry %= least_common_mult

        return (
            worry,
            self.test_on_success
            if (worry % self.test_mod) == 0
            else self.test_on_failure,
        )


def __read_num(line: str) -> int:
    return int(re.search("\d+", line).group())


def __read_nums(line: str) -> List[int]:
    return [int(x) for x in re.findall("\d+", line)]


def day11(file: str, count: int, relief: bool = False):
    m = None
    monkeys = {}

    for l in read_one(file):
        if l.startswith("Monkey"):
            if m is not None:
                monkeys[m.id] = m
            m = Monkey(__read_num(l))
        elif l.startswith("Starting items:"):
            m.items += __read_nums(l)
        elif l.startswith("Operation:"):
            [*_, arg1, op_func, arg2] = l.split(" ")
            m.op_func = op_func
            m.op_args = [x if x == "old" else int(x) for x in [arg1, arg2]]
        elif l.startswith("Test:"):
            m.test_mod = __read_num(l)
        elif l.startswith("If true:"):
            m.test_on_success = __read_num(l)
        elif l.startswith("If false:"):
            m.test_on_failure = __read_num(l)

    monkeys[m.id] = m
    least_common_mult = lcm(*[v.test_mod for v in monkeys.values()])

    for _ in range(count):
        for m in monkeys.values():
            items = [*m.items]
            m.items = []
            for x in items:
                (next_worry, next_m) = m.process(x, relief, least_common_mult)
                monkeys[next_m].items.append(next_worry)

    counters = [v.totals_inspects for v in monkeys.values()]
    counters.sort()
    return counters[-2] * counters[-1]


assert day11("test11", 20, True) == 10605
assert day11("test11", 10_000) == 2_713_310_158

print("Part1:\t", day11("input11", 20, True))
print("Part2:\t", day11("input11", 10_000))
