#!/usr/bin/python3
for indx in range(122, 96, -1):
    if indx % 2 == 0:
        alpha = chr(indx)
    else:
        alpha = chr(indx-32)
    print("{}".format(alpha), end="")
