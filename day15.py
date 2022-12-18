from utils import read_one
from typing import Tuple, List
import re
from dataclasses import dataclass

Point = Tuple[int, int]


@dataclass
class SensorReading:
    sensor: Point
    beacon: Point
    dist: int

    @classmethod
    def init(cls, sensor: Tuple[int, int], beacon: Tuple[int, int]):
        return cls(
            sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        )


def flatten(ranges: List[Tuple[int, int]]):
    result = []
    for r in ranges:
        if len(result) > 0 and r[0] <= result[-1][1]:
            prev = result.pop()
            result.append((prev[0], max(prev[1], r[1])))
        else:
            result.append(r)
    return result


def read_state(file: str) -> List[SensorReading]:
    sensors = []
    for l in read_one(file):
        [sx, sy, bx, by] = [int(x) for x in re.findall(r"[-]?\d+", l)]
        sensors.append(SensorReading.init((sx, sy), (bx, by)))
    return sensors


def day15_1(file: str, y: int):
    points_on_y = set([])
    nothing_ranges_on_y = set([])
    readings = read_state(file)
    for reading in readings:
        sx, sy = reading.sensor
        dist = reading.dist
        points_on_y.update(
            [rx for rx, ry in [reading.sensor, reading.beacon] if y == ry]
        )
        abs_y_dist = abs(y - sy)
        if abs_y_dist < dist:
            nothing_ranges_on_y.update(
                [*range(sx - dist + abs_y_dist, sx + 1 + dist - abs_y_dist)]
            )

    return len(nothing_ranges_on_y.difference(points_on_y))


def day15_2(file: str, min_val: int, max_val: int):
    result = 0, 0
    readings = read_state(file)
    for y in range(min_val, max_val + 1):
        points_on_y = []
        for reading in readings:
            sx, sy = reading.sensor
            dist = reading.dist
            abs_y_dist = abs(y - sy)
            if abs_y_dist < dist:
                points_on_y.append(
                    (
                        max(0, sx - dist + abs_y_dist),
                        min(max_val + 1, sx + 1 + dist - abs_y_dist),
                    )
                )
        ranges = flatten(sorted(points_on_y, key=lambda x: x[0]))
        if len(ranges) == 2:
            result = ranges[0][1], y
            break

    return result[0] * 4_000_000 + result[1]


assert day15_1("test15", 10) == 26
assert day15_2("test15", 0, 20) == 56_000_011
print("Part1:\t", day15_1("input15", 2_000_000))
print("Part2:\t", day15_2("input15", 0, 4_000_000))
