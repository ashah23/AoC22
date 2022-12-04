def read_from_file(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append((line))
    return lines