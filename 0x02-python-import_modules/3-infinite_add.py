#!/usr/bin/python3
def addarg(argv):
    length = len(argv) - 1
    if length == 0:
        print("{:d}".format(length))
        return
    else:
        i = 1
        total = 0
        while i <= length:
            total = total + int(argv[i])
            i = i + 1
        print("{:d}".format(total))


if __name__ == "__main__":
    import sys
    addarg(sys.argv)
