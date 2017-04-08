import sys

from anyreader import anyread

if __name__ == '__main__':
    filename = sys.argv[1]
    print(anyread(filename))