import argparse
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
