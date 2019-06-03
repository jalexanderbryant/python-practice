# Task: Implement find
#X v1: find <starting dir>
#X v2: find <starting dir> -name "*.txt"
#X v3: find <starting dir> -type d
import argparse
import glob
import os
class Cmd(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("dir",
                            help="The starting directory", nargs='?',
                            type=str)
        parser.add_argument("-name", help="Filter by name", type=str)
        parser.add_argument("-type", help="Filter by type", type=str)
        self._top_level_args = parser.parse_args()

    def find(self):
        path = self._top_level_args.dir if self._top_level_args.dir else '.'
        path += '/**' # Modify path to search in subdirectories

        if self._top_level_args.name:
            path += '/%s' % self._top_level_args.name

        for name in glob.iglob(path, recursive=True):
            if self._top_level_args.type == 'd' and not os.path.isdir(name):
                continue
            print(name)


if __name__ == '__main__':
    Cmd().find()
