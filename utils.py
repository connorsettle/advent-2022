def read_one(filename, trim=True):
    f = open(f"data/{filename}.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        yield line.strip() if trim else line
    f.close()


def read_many(filename, line_count=1, trim=True):
    f = open(f"data/{filename}.txt", "r")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines += [line.strip() if trim else line]
        if len(lines) == line_count:
            yield lines
            lines = []
    f.close()
