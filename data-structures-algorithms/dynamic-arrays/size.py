import sys  # provides getsizeof

def print_size(n):
    
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)     # Size of data list in bytes
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))

        data.append(1)       # Increment size of data by one

if __name__ == '__main__':
    print_size(27)