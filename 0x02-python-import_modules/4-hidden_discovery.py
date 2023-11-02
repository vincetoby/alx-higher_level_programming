#!/usr/bin/python3
import hidden_4


def discover_hidden():
    hid_names = dir(hidden_4)
    for i in hid_names:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    discover_hidden()
