import argparse, sys

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delimiter", help="Delimeter")
    parser.add_argument("-f", "--field", help="Field(s)")
    # parser.add_argument("file", help="Input file.", type=str, required=False)
    args = parser.parse_args()
    return args

def cut(args):
    
    for line in sys.stdin.readlines():
        out_line = None
        if(args.delimiter):
            out_line = line.strip().split(args.delimiter)

        if(args.field):
            if '-' in args.field:
                # fields = args.field.split('-')
                fields = [int(f) for f in args.field.split('-')]  
                out_line = out_line[fields[0]-1 : fields[1]]
            else:
                out_line = out_line[int(args.field)-1]
                


        print(" ".join(out_line))

    pass

if __name__ == '__main__':
    args = init_argparser()
    cut(args)