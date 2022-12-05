def lines(filename, cb):
    L = []  # Declare empty array
    with open(filename, 'r') as f:
        L = f.readlines()

    # Return array with newline chars stripped, containing return value of callback function
    return [cb(line.rstrip()) for line in L]