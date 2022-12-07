from utils import read_one


def get_path(current_path, node):
    return str.join("/", [*current_path, node])


def parse_state(file):
    current_path = []
    dirs = [""]
    files = []
    for line in read_one(file):
        if line.startswith("$ "):
            cmd = line[2:]
            if cmd == "cd /":
                current_path = [""]
            elif cmd == "cd ..":
                current_path.pop()
            elif cmd.startswith("cd "):
                current_path.append(cmd[3:])
        else:
            if line.startswith("dir "):
                dirs.append(get_path(current_path, line[4:]))
            else:
                size, filename = line.split(" ")
                files += [(int(size), get_path(current_path, filename))]
    return dirs, files


def day07_1(file):
    dirs, files = parse_state(file)
    totals = [
        sum([size for (size, filename) in files if filename.startswith(f"{dir}/")])
        for dir in dirs
    ]
    return sum([x for x in totals if x <= 100_000])


def day07_2(file):
    filesystem_space = 70_000_000
    required_space = 30_000_000

    dirs, files = parse_state(file)
    to_delete = (
        sum([size for (size, filename) in files]) - filesystem_space + required_space
    )
    totals = [
        sum([size for (size, filename) in files if filename.startswith(f"{dir}/")])
        for dir in dirs
    ]
    return min(*[size for size in totals if size >= to_delete])


assert day07_1("test07") == 95_437
assert day07_2("test07") == 24_933_642
print("Part1:\t", day07_1("input07"))
print("Part2:\t", day07_2("input07"))
