import argparse

# need to implement
#   - 3 flag arguments (these trigger actions if they are in the command)
#   - 3 optional arguments (these take an argument and set a variable in the
#           script to the value of that option)
#   - positional arguments (lists of files at the end of all the '-' style args
#       and can handle wildcards like */.txt


parser = argparse.ArgumentParser()

# lets start with a positional argument
parser.add_argument("square", help="display a square of a given number",
                    type=int)

# Now lets add an optional argument
# Expects one argument to be specified
# - Without action=store_true, will accept arbitrary integer value
# - With action=store_true, takes no arguments, but sets var to true if it is
#   present (now a flag argument)
parser.add_argument("-v", "--verbosity", help="Increase output verbosity",
                    type=int, choices=[0,1,2])

# One more positional argument
parser.add_argument('files', help="File or list of files.", nargs='+')

# Parse args
args = parser.parse_args()

answer = args.square**2

# Print some output
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)


print(args.files)
