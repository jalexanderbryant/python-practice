# handle -help or -h
# 3+ flag arguments: -flag (like -f -rf)
# 3+ options: -arg - value
# positional argument: occurs at the end of all the -arg arguments
import sys
print(sys.argv)

"""
45 minute drill
"""

def handle_args(args):
    for i in range(len(args)):
        if (args[i] == "-h") or (args[i] == "-help"):
            print("HELP")
        elif(args[i].startswith('-') and
             (i+1) < (len(args)) and not args[i + 1].startswith('-')):
                arg = args[i][1:]
                print(arg,":", args[i + 1])
        elif(args[i].startswith('-')):
            flags = args[i][1:]
            flags = [x for x in flags]
            if 'r' in flags:
                print("Recursive")
            if 'f' in flags:
                print("Force")
            if 'x' in flags:
                print('Handles X flag')

handle_args(sys.argv)
"""
Post 45 minute drill
"""
def handle_args2(sys.argv):
    

handle_args2(sys.argv)




