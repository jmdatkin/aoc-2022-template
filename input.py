def lines(filename, cb):
    L = []
    with open(filename, 'r') as f:
        L = f.readlines()

    return [cb(line.rstrip()) for line in L]