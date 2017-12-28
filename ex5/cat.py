# Cat
# Reimplement the cat command
#   Print file to screen
    # Read command line args: cat filename
    # Open file
    # Read file and print
#   Get command line args 
#   Print file to screen
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("files", nargs='+', type=str, help="files to be concatenated")
parser.add_argument('-n', action='store_true')
parser.add_argument('-e', action='store_true')
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

print(args.files)
# Use if -n flag is set
line_count = 0

# Open the file
for file in args.files:
    f = open(file, "r")
    for line in f:
        output_line = line.rstrip()
        if args.n:
            line_count += 1
            output_line = "{:>5}  {}".format(line_count, output_line)
        if args.e:
            output_line = "{}$".format(output_line)
        if args.t:
            output_line = output_line.replace("\t", "^I")

        print(output_line)

# 15 Minutes to get just the concatenation working.
# Process:
  # Right out what i wanted to accomplish in english,
  # Break down steps
  # Had to look up opening and reading files in python. As well as
  # stripping white space from the of the line
  # Looked throught argparse docs to figure out how to do multiple files
# In the remaining time I revised the logic and added 3 additional flag options.
# Got slowed down by revisting the terminal periodically to test expressions and check
# stack overflow for tasks like replacing every occurence of a chacter in a string with another.
# Flipped back and forth to the terminal to see how the actual command outputs lines. I could
# cut down on some time not spent developing by focusing solely writing the logic and getting basic output,
# without worrying about replicating the original command perfectly. Once the logic is in place,
# I could go back and 

