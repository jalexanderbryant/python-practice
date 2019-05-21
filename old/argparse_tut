import argparse
"""
parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("-fn", "--filename", help="what's the file")
# parser.add_argument("-v", "--verbosity", help="How verbose")
# parser.add_argument("--something", help="add an option value")
parser.add_argument("-r", help="recursive", action="store_true")
parser.add_argument("-f", help="force", action="store_true")

args = parser.parse_args()
if args.r:
    print("recursive")
if args.f:
    print("force")
"""


"""
Positional Arguments
  - Required arguments we need for our program to complete.
  - Do not require dash(-) because they're not optional

Optional Arguments
  - -h option is builtin by default
  - can reate as many as we like and argparse will handle it

MUX (Mutually Exclusive Arguments)
  - Can select one option or another
  - Can be Done with a group
  - Automatically generates an output telling the user you can only pick one, should they try to use both.
"""


# Fibonacci
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("num", help="The Fibonacci number" +
        " you wish to calculate", type=int)

    parser.add_argument("-o", "--output",  help="Output the " 
       "result to a file", action="store_true")

    parser.add_argument("--filename", help="Specify the name "
      "of the output file")

    args = parser.parse_args()

    result = fib(args.num)
    if(args.verbose):
        print("The " + str(args.num) + " the fibonacci number is " + str(result))
    elif(args.quiet):
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result))


    if(args.output):
        if(args.filename):
            f = open(str(args.filename) + ".txt", "a")
        else:
            f = open("fibonacci.txt", "a")
        f.write(str(result) + '\n')


if __name__ == '__main__':
    Main()
