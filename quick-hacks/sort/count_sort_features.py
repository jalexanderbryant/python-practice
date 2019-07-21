import sys

def count_features(lines):
    if len(lines) == 0:
        return 0;
    else:
        line = lines[0].strip()

        if len(line) > 1 and line[0] == '-':
            return 1 + count_features(lines[1:])
        else:
            return 0 + count_features(lines[1:])

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    print(type(lines))
    print(count_features(lines))
    sys.exit()
