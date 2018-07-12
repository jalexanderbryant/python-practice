import re, os, argparse, glob

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_pattern")
    parser.add_argument("file_pattern")
    args = parser.parse_args()
    # print(args)
    return args

# Grep
def grep(args):
    # Use glob to match file pattern
    for name in glob.iglob(args.file_pattern):
        matched_file = open(name, 'r')
        for line in matched_file.readlines():
            match = re.search(args.search_pattern, line)
            if match:
                print(line.strip())

# Entry point - Any additional setup can be done here
def Main():
    grep(init_argparse())

# Test
if __name__ == '__main__':
    Main()

