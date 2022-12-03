from utils import read_one


def get_min_index(items):
    index = 0
    val = items[0]
    for i, r in enumerate(items):
        if r < val:
            index = i
            val = r
    return index


def insert_local_max(max, localMax):
    currentMinMaxIdx = get_min_index(max)
    max[currentMinMaxIdx] = (
        localMax if localMax > max[currentMinMaxIdx] else max[currentMinMaxIdx]
    )


def day01(file, total_size=1):
    max = [0] * total_size
    localMax = 0
    for line in read_one(file):
        if len(line) == 0:
            insert_local_max(max, localMax)
            localMax = 0
        else:
            localMax += int(line)
    insert_local_max(max, localMax)
    return sum(max)


assert day01("test01") == 24000
assert day01("test01", 3) == 45000
print("Part1:\t", day01("input01"))
print("Part2:\t", day01("input01", 3))
