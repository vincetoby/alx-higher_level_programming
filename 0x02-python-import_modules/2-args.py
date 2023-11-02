#!/usr/bin/python3
def print4me(argv):
    length = len(argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
        return
    else:
        if length == 1:
            print("{:d} argument:".format(length))
        else:
            print("{:d} arguments:".format(length))
        indx = 1
        while indx <= length:
            print("{:d}: {:s}".format(indx, argv[indx]))
            indx = indx + 1


if __name__ == "__main__":
    import sys
    print4me(sys.argv)
