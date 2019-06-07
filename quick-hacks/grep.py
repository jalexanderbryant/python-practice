# Task: Implement grep
# v1: empty string always matches
# v2: find first matching pattern in file with RE

# X modify find to iterate over all files by the provided file pattern
 #X  Error and exit if pattern is a directory
# X Open each file
# X iterate over each line in file
# if its a match,
    # X Print the file name,
    # X print any line that resultied in a match
import argparse
import glob
import os
import sys
import re

class Cmd(object):
    def __init__(self):
        print(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("search_pattern",
                            help="The pattern to search for in each file.",
                            type=str)
        parser.add_argument("file_pattern",
                            help="The file name pattern to search in.",
                            type=str)

        self._args = parser.parse_args()
        print(parser.parse_known_args())

    def grep(self):
        path = self._args.file_pattern
        if os.path.isdir(path):
            print("grep: %s: Is a directory" % path)
            sys.exit()
       # path += '/**' # Modify path to search in subdirectories

        #if self._args.name:
        #    path += '/%s' % self._args.name

        for name in glob.iglob(path, recursive=True):
            print(name)
            pattern_found = False
            with open(name, 'r') as f:
                for line in f:
                    if self._args.search_pattern != '':
                        # Perform searching
                        if not re.search(self._args.search_pattern, line):
                            continue
                    # always print
                    print(line)

if __name__ == '__main__':
    Cmd().grep()
