# import packages
# Setup arguments (input, filepattern/name)
# load single file, iterate over lines
# Check line for input string
  # If there, print file_name:line
  # Else continue
import re
import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_pattern",
                        type=str, help="Pattern to find in file.")
    parser.add_argument("file_pattern", nargs='+',
                        help="File pattern to search within")
    args = parser.parse_args()
    # print("search pattern: ", args.search_pattern)
    # print("file pattern: ", args.file_pattern)
    return args

def run():
    args = parse_args()

    # Load File(s)
    for file in args.file_pattern:
        file = open(file, 'r')
        for line in file:
            line = line.strip('\n')
            if re.search(args.search_pattern, line):
                print("{}: {}".format(file.name, line))

define search(search_string):


# MAIN START
# run()