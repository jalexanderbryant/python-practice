import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delimiter", type=str, help="Sets a delimiter")
    parser.add_argument("-f", "--fields", type=str, help="Sets a delimiter")
    args = parser.parse_args()
    print("delimeter: ", args.delimiter)
    print("fields: ", args.fields)
    return args


def get_input():
    input_stream = sys.stdin.read()
    input_stream = input_stream.split('\n')
    # print("input:", input_stream[0])
    return input_stream


def run():
    # Setup args
    args = parse_args()

    # Read input from the stream
    stream = get_input()

    fields = args.fields
    if '-' in fields:
        fields = fields.split('-')
        print("FIELDS", fields)


    for line in stream:
        line = line.split(args.delimiter)
        if type(fields) is list:
            start = int(fields[0])
            end = int(fields[1])
            output = line[start-1:end]
            print(' '.join(output))
        else:
            # Check if field is in range
            field = int(fields)
            if (field-1) < len(line):
              print(line[field-1])


            # output = line[field-1]
            # print(' '.join(output))
# Read input from stram
# Read input line by line


run()
