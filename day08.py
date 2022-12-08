from utils import read_one


def parse_tree(file):
    treesStr = [list(x) for x in read_one(file)]
    trees = [[int(y) for y in x] for x in treesStr]
    width = len(trees[0])
    height = len(trees)
    return trees, width, height


def day08_1(file):
    trees, width, height = parse_tree(file)
    state = [[0] * (width - 2) for _ in trees[1 : height - 1]]

    # Horizontal
    for i in range(1, height - 1):
        minLeft = int(trees[i][0])
        minRight = int(trees[i][width - 1])
        for j in range(1, width - 1):
            val = trees[i][j]
            if val > minLeft:
                state[i - 1][j - 1] = 1
                minLeft = val

            jInvert = width - j - 1
            val = trees[i][jInvert]
            if val > minRight:
                state[i - 1][jInvert - 1] = 1
                minRight = val

    # Vertical
    for j in range(1, width - 1):
        minTop = int(trees[0][j])
        minBottom = int(trees[height - 1][j])
        for i in range(1, height - 1):
            val = trees[i][j]
            if val > minTop:
                state[i - 1][j - 1] = 1
                minTop = val

            iInvert = height - i - 1
            val = trees[iInvert][j]
            if val > minBottom:
                state[iInvert - 1][j - 1] = 1
                minBottom = val

    edges = (height + width - 2) * 2
    inner = sum([sum(x) for x in state])
    return edges + inner


def day08_2(file):
    trees, width, height = parse_tree(file)
    result = 0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            val = trees[i][j]
            current = 1
            counters = [0] * 4
            pointers = [1] * 4
            left, right, top, bottom = [*range(0, 4)]

            # Check trees to the left
            while j >= pointers[left] and val > trees[i][j - pointers[left]]:
                counters[left] += 1
                pointers[left] += 1
            current *= counters[left] + 1 if j >= pointers[left] else counters[left]

            # Check trees to the right
            while j + pointers[right] < width and val > trees[i][j + pointers[right]]:
                counters[right] += 1
                pointers[right] += 1
            current *= (
                counters[right] + 1 if j + pointers[right] < width else counters[right]
            )

            # Check trees to the top
            while i >= pointers[top] and val > trees[i - pointers[top]][j]:
                counters[top] += 1
                pointers[top] += 1
            current *= counters[top] + 1 if i >= pointers[top] else counters[top]

            # Check trees to the bottom
            while (
                i + pointers[bottom] < height and val > trees[i + pointers[bottom]][j]
            ):
                counters[bottom] += 1
                pointers[bottom] += 1
            current *= (
                counters[bottom] + 1
                if i + pointers[bottom] < height
                else counters[bottom]
            )

            if current > result:
                result = current

    return result


assert day08_1("test08") == 21
assert day08_2("test08") == 8
print("Part1:\t", day08_1("input08"))
print("Part2:\t", day08_2("input08"))
