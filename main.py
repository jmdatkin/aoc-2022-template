import input

FILENAME = "input"

def cb(line):
    return line

if __name__ == "__main__":
    lines = input.lines(FILENAME, cb)
    print(lines)
