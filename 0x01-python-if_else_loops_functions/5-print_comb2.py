#!/usr/bin/python3
for indx in range(0, 100):
    if indx != 99:
        print("{:02d}, ".format(indx), end="")
    else:
        print("{:02d}".format(indx))
