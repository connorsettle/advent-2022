def read_one(filename):
    f = open(f"data/{filename}.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        yield line.strip()
    f.close()


def read_many(filename, line_count=1):
    f = open(f"data/{filename}.txt", "r")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines += [line.strip()]
        if len(lines) == line_count:
            yield lines
            lines = []
    f.close()
