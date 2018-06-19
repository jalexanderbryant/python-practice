import argparse

def init_argparser():
  parser = argparse.ArgumentParser()
  parser.add_argument("files", help="Files to concatenate", nargs='+', type=str)
  parser.add_argument("-n", help="Number the output lines, starting at 1",
    action="store_true")
  parser.add_argument("-e", action="store_true")
  parser.add_argument("-t", action="store_true")
  args = parser.parse_args()
  return args

def Main():
  args = init_argparser()
  print("list of files: " + ', '.join(args.files))

  line_count = 0

  for file in args.files:
    # Open file...
    try:
      fp = open(file, 'r')
      for line in fp:
        out_line = line.rstrip()
        if args.n:
          line = "{:>5}\t{}".format(line_count+1, out_line)
        print(line)
        line_count += 1
      
      fp.close()
    except FileNotFoundError as e:
      print(e)
      return 1

if __name__ == '__main__':
 Main()
"""
Read command...
Iterate over list of files
  For each file over each file
  If Output file specified
    write to output file
  Else
    write to standard output
Return 0
"""