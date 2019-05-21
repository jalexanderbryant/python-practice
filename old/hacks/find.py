"""
Find.py
Implement:
  - name filter
  - type filer
  - print action
  - exec action

  find . -name "*.txt" -print

"""


import glob, os, argparse, subprocess, sys

def init_argparser():
  parser = argparse.ArgumentParser()
  parser.add_argument("dir", nargs='?', default='.')
  parser.add_argument("-name", help="Filters by file name", type=str, default='*')
  parser.add_argument("-type", help="Filters by file type", type=str)
  parser.add_argument("-print", help="Print each file path to standard output", action="store_true")
  parser.add_argument("-exec", help="Perform specified action on each file", nargs='*')
  args = parser.parse_args()
  print(args)
  return args

def find(args, path):

  # print directory
  print(path)


  # Use glob to scan directory
  for name in glob.iglob(path + '/**/' + args.name, recursive=True):
    # TODO - Add code for hidden files
    if args.type: 
      # Print only directories
      if args.type == 'd' and not os.path.isdir(name):
        # print("{} is NOT a directory".format(name))
        continue
      # Print only regular files
      if args.type == 'f' and os.path.isdir(name):
        continue
    if args.print or not args.exec:
      print(name)
    elif args.exec:
      try:
        ind = args.exec.index('{}')
        args.exec.remove(';')

      except ValueError as e:
        print("Error in action. Command must include '\{\}'")
        sys.exit
      args.exec[ind] = name
      print(args.exec)
      p = subprocess.Popen(args.exec)

def Main():
  args = init_argparser()
  find(args, args.dir)

# Test
if __name__ == '__main__':
  Main()