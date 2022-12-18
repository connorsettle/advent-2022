from utils import read_one
from dataclasses import dataclass
import sys
from typing import Tuple, List
from enum import Enum


class Fill(Enum):
    EMPTY = 0
    ROCK = 1
    SAND = 2


Point = Tuple[int, int]


@dataclass
class Cave:
    __drop_x: int
    __max_x = -sys.maxsize
    __max_y = -sys.maxsize
    __min_x = sys.maxsize
    __min_y = 0
    __grid: List[List[int]] = None

    @classmethod
    def init(cls, drop_x: int, data: List[List[Point]]):
        vectors = []
        c = Cave(drop_x)
        for points in data:
            c.__min_x = min(c.__min_x, *[x for (x, _) in points])
            c.__max_x = max(c.__max_x, *[x for (x, _) in points])
            c.__max_y = max(c.__max_y, *[y for (_, y) in points])
            vectors += [(x, points[i + 1]) for i, x in enumerate(points[:-1])]
        c.__grid = [
            [Fill.EMPTY if i != c.__height - 1 else Fill.ROCK for _ in range(c.__width)]
            for i in range(c.__height)
        ]
        for v in vectors:
            c.__add_rock(v)
        return c

    @property
    def drop_point(self) -> Point:
        return self.__offset_point((self.__drop_x, self.__min_y))

    @property
    def __height(self) -> int:
        return self.__max_y - self.__min_y + 3

    @property
    def __width(self) -> int:
        return self.__max_x - self.__min_x + 3

    def __offset_point(self, p: Point):
        return (p[0] - self.__min_x + 1, p[1])

    def __add_rock(self, v: Tuple[Point, Point]):
        (x1, y1), (x2, y2) = v
        orig_points = (
            [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
            if x1 == x2
            else [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
        )
        self.__set_fill(Fill.ROCK, *[self.__offset_point(p) for p in orig_points])

    def __set_fill(self, fill: Fill, *points: Point):
        for p in points:
            self.__grid[p[1]][p[0]] = fill

    def __add_col(self, start=True):
        for i, row in enumerate(self.__grid):
            row.insert(
                0 if start else len(row),
                Fill.EMPTY if i != len(self.__grid) - 1 else Fill.ROCK,
            )

    def __next_filled_y(self, p: Point):
        return next(
            (
                y
                for y, val in enumerate(self.__grid)
                if y >= p[1] and val[p[0]] != Fill.EMPTY
            ),
        )

    def drop_til_reached_floor(self, p: Point) -> bool:
        next_filled_y = self.__next_filled_y(p)

        if next_filled_y == len(self.__grid) - 1:
            return False
        curr = p[0], next_filled_y - 1

        for x_offset in [-1, 1]:
            if self.__grid[curr[1] + 1][curr[0] + x_offset] == Fill.EMPTY:
                return self.drop_til_reached_floor((curr[0] + x_offset, curr[1] + 1))

        self.__set_fill(Fill.SAND, curr)
        return True

    def drop_til_point_is_filled(self, p: Point, stop_point: Point) -> bool:
        next_filled_y = self.__next_filled_y(p)
        curr = p[0], next_filled_y - 1

        if curr[0] == 0:
            self.__add_col()
            curr = curr[0] + 1, curr[1]
            self.__min_x -= 1
            stop_point = (stop_point[0] + 1, stop_point[1])
        elif curr[0] == len(self.__grid[0]) - 1:
            self.__add_col(False)

        for x_offset in [-1, 1]:
            if self.__grid[curr[1] + 1][curr[0] + x_offset] == Fill.EMPTY:
                return self.drop_til_point_is_filled(
                    (curr[0] + x_offset, curr[1] + 1), stop_point
                )

        self.__set_fill(Fill.SAND, curr)
        return stop_point[0] != curr[0] or stop_point[1] != curr[1]


def day14_1(file: str):
    cave = Cave.init(
        500,
        [
            [tuple([int(y) for y in x.split(",")]) for x in l.split(" -> ")]
            for l in read_one(file)
        ],
    )
    counter = 0
    while cave.drop_til_reached_floor(cave.drop_point):
        counter += 1
    return counter


def day14_2(file: str):
    cave = Cave.init(
        500,
        [
            [tuple([int(y) for y in x.split(",")]) for x in l.split(" -> ")]
            for l in read_one(file)
        ],
    )
    counter = 0
    while cave.drop_til_point_is_filled(cave.drop_point, cave.drop_point):
        counter += 1
    return counter + 1


assert day14_1("test14") == 24
assert day14_2("test14") == 93
print("Part1:\t", day14_1("input14"))
print("Part2:\t", day14_2("input14"))
