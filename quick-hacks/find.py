# Task: Implement find
#X v1: find <starting dir>
#X v2: find <starting dir> -name "*.txt"
#X v3: find <starting dir> -type d
#X v4: -type f
#X v5: -exec {} \;
#X v5: -perm xxx
import argparse
import glob
import os
import sys
class Cmd(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("dir",
                            help="The starting directory", nargs='?',
                            type=str)
        parser.add_argument("-name", help="Filter by name", type=str)
        parser.add_argument("-type", help="Filter by type", type=str)
        parser.add_argument("-exec", help="Action to perform", type=str)
        self._top_level_args = parser.parse_args()

    def find(self):
        print(sys.argv)
        path = self._top_level_args.dir if self._top_level_args.dir else '.'
        path += '/**' # Modify path to search in subdirectories

        if self._top_level_args.name:
            path += '/%s' % self._top_level_args.name

        for name in glob.iglob(path, recursive=True):
            if self._top_level_args.type == 'd' and not os.path.isdir(name):
                continue
            if self._top_level_args.exec:
                # do stuff here
                self.__exec()
            else:
                print(name)


    def __exec(self):
        print('test')
        e_parser = argparse.ArgumentParser()
        #e_parser.add_argument("subcmd", help="Subcommand to be run by -exec.",
        #                        type=str)
        #exec_args = e_parser.parse_args()

if __name__ == '__main__':
    Cmd().find()
