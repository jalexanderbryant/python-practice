# Goal: Make an implementation of the sed command
# v1: Just work with the input stream: 
#     ls -l | sed "s/jamesbryant/cynicalneon/"
#     - find the specified string and replace with static string

# v2: Use sed formatting to replace the string

# v3: Use Sed formatting.



import argparse
import glob
import os
import sys
import re

class Sed(object):
    def __init__(self):
        # Setup args
        # Parse pattern string
        # Return components of pattern string
        #   replacement_string
        #   search_pattern
        print(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("function",
                            help="""The sed function used. Contains the regex 
                            search pattern and substitution string.""",
                            type=str)
        self.__args = parser.parse_args()
        self.__search_pattern = None
        self.__sub_pattern = None

        print(parser.parse_known_args())
        self.__search_pattern, self.__sub_pattern = self.__parse_function()

    def __parse_function(self):
        pattern = self.__args.function.split('/')
        print(pattern)
        return (pattern[1], pattern[2])
        

    def sed(self):
        # Read string from standard input
        for line in sys.stdin:
            # check if searched_string in line
            # v1, v3 completed with the 2 lines below
            #if self.__search_pattern in line:
            #    line = line.replace(self.__search_pattern, self.__sub_pattern)

            """ These 3 lines below do not work."""
            #if re.match(self.__search_pattern, line) is not None:
            #    print("something")
            #    line = line.replace(self.__search_pattern, self.__sub_pattern)
            line = re.sub(self.__search_pattern, self.__sub_pattern, line)
            print(line, end="")

if __name__ == '__main__':
    Sed().sed()
