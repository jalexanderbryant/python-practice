import argparse
import sys
import os
import random

class Sort(object):
    def __init__(self):
        print(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("FILE",
                            help = "File to read from.",
                            type = str,
                            nargs = '?')
        parser.add_argument("-r", "--reverse",
                            help = "Reverse the sort order.",
                            action='store_true')
        parser.add_argument("-o", "--output",
                            help = "Write result to file.",
                            type = str)
        parser.add_argument("-f", "--ignore-case",
                            help = "Ignore case",
                            action = 'store_true',
                            default=False)
        parser.add_argument("-R", "--random-sort",
                            help = "Randomize sorting.",
                            action = "store_true")

        parser.add_argument("-V", "--annotate",
                            help = "Annotate part of text used for sorting.",
                            action = "store_true")

        self.__args = parser.parse_args()
        print(parser.parse_known_args())


    def __read_standard_input(self):
        stdin_lines = sys.stdin.read().splitlines()
        return stdin_lines


    def __print_lines(self, lines, annotate=False):
        for line in lines:
            print(line)


    def __standard_sort(self, lines, ignore_case=False):
        if self.__args.ignore_case:
            lines.sort(key=str.upper)
        else:
            lines.sort()
        return lines


    def __reverse(self, lines):
        lines.reverse()
        return lines

    def __randomize_lines(self, lines):
        random.shuffle(lines)
        return lines


    def __handle_sorting(self, lines):
        if self.__args.random_sort:
            s_lines = self.__randomize_lines(lines)
        else:
            s_lines = self.__standard_sort(lines, self.__args.ignore_case)

        if self.__args.reverse:
            s_lines = self.__reverse(s_lines)

        return s_lines


    def __write_to_file(self, lines, filename):
        if os.path.exists(filename):
            os.remove(filename)
        output_file = open(filename, 'w')
        for line in lines:
            output_file.write("{}\n".format(line))

        output_file.close()


    def sort(self):
        if self.__args.FILE is None or self.__args.FILE == '-':
            # Read from STDIN
            unsorted_lines = self.__read_standard_input()

            # Handle Sorting
            sorted_lines = self.__handle_sorting(unsorted_lines)

            # Handle Printing or writing to file
            if self.__args.output:
                self.__write_to_file(sorted_lines, self.__args.output)
            else:
                self.__print_lines(sorted_lines, self.__args.annotate)


if __name__ == '__main__':
    Sort().sort()
