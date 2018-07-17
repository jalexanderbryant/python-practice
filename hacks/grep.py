import glob, os, argparse, re, sys

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_pattern", help="Pattern to search for", nargs=1)
    # parser.add_argument("file_pattern", help="File to search", type=str)
    args = parser.parse_args()
    return args

def grep(args):
    print(args)


def Main():
    args = init_argparser()
    grep(args)
    # Handle opening files
    # res = re.match(r"*.txt")
    # print(res)

 
    print("List of args\n")
    print(args)


if __name__ == '__main__':
    Main()
