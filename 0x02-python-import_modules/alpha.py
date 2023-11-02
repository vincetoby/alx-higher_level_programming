#!/usr/bin/python3
def print_alph():
    for i in range(97, 123):
        i = i - 32
        print("{}".format(chr(i)), end="")
    print()


print_alph()
