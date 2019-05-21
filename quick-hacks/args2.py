import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")

# action=count - lets us count the # of occurrences of a specific optional
# argument. Example: -v, -vv, -vvv, -vvvv
# Again, we make it like a flag. 
# default=0 lets us compare verbosity count (can't compare None to int, so we
# force a default integer value in case no -v is provided)
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity", default=0)
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
