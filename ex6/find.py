# Implement find. 

# find . -name "*.txt" -print
# For 'find' basics, here's what i want to implement...
#   Directory (always needed): find <dir>
#       should print files in provided directory
#   filter argument:
#       1) find <dir> -name <name or wildcard>
#           should print file names in provided directory filtered by name
#       2) find <dir> -type <type>
#           should print file names in provided directory filtered by name
#   Action:
#       default action is print. Will use unless something else is specified
import argparse
import subprocess
import glob
import os
import copy

# MAIN START
parser = argparse.ArgumentParser()
parser.add_argument("dir", type=str, help="Name of directory")
parser.add_argument("-name", type=str, help='Applies name filter')
parser.add_argument("-type", type=str, help="Applies type filter")
parser.add_argument("-exec", nargs='+', type=str, help="Applies exec function")
args = parser.parse_args()

path = "{}/**".format(args.dir)

# Add na
if args.name:
    path = path + "/{}".format(args.name)


# print(args.dir)
for item in glob.iglob(path, recursive=True):
    # Check types
    if(args.type == 'd') and (not os.path.isdir(item)):
        continue
    if(args.type == 'f') and (not os.path.isfile(item)):
        continue
    if(args.type == 'l') and (not os.path.islink(item)):
        continue

    if(args.exec):
        cmd = copy.copy(args.exec)
        cmd = cmd[0].split(' ')
        ind = cmd.index('{}')
        cmd[ind] = item
        print("command to run: ", cmd)
        subprocess.call(cmd)
    else:
        print(item)

