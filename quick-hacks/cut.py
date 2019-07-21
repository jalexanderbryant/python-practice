# Task: Implement cut command

import argparse
import glob
import os
import fileinput
import sys

class Cut(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", help="Delimeter", type=str)
        parser.add_argument("-f", help="Fields", type=str)
        self._top_level_args = parser.parse_args()
        print('action=__init__ top_level_args=%s', self._top_level_args)

    def cut(self):
        # for name in glob.iglob("*", recursive=False):
        #    print(name)
        for line in sys.stdin.readlines():
            self._process(line)

    def _process(self, line):
        if self._top_level_args.d:
            line = self._split(line)
        if self._top_level_args.f:
            line = self._get_by_field(line)
        print(line)

    def _split(self, line):
        return line.split(self._top_level_args.d)

    def _get_by_field(self, arr):
        if self._top_level_args.find('-') is not -1:
            arr = arr.split('-')
            arr = arr[arr[0]:arr[1]]


if __name__ == '__main__':
    Cut().cut()
