#V1: cat a.txt b.txt c.txt
# Initialize parse arg
# add arguments
# For each file in the file argument
#   open the file
#   iterate over each line in the file:
    # Print the text
# V2: cat a.txt b.txt c.txt > d.txt
    # Open a file stream for a new file
    # Write the outputs of the previous files into the new file
# V3: Implement an additional argument
import argparse

class Cat(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("files",
                            help="File or list of files to concatenate",
                            nargs="+")
        parser.add_argument("-n", "--number", help="Number all output lines",
                            action="store_true")
        self._top_level_args = parser.parse_args()

    def command(self):
        #print(self._top_level_args.files)
        #print(type(self._top_level_args.files))
        line_no = 0
        for filename in self._top_level_args.files:
            with open(filename, 'r') as f:
                for line in f:
                    if self._top_level_args.number:
                        line = "%s %s" % (str(line_no), line)
                        line_no += 1
                    print(line.strip())

                #print("\n") # Newline character to break up file output

if __name__ == '__main__':
    # Start doing stuff
    Cat().command()
