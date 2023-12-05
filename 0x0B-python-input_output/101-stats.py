#!/usr/bin/python3
import sys
import io


dictstat = {}
tsize = 0
tcount = 0
for line in sys.stdin:
    split_line = line.split()
    stat = split_line[-2]
    tsize += int(split_line[-1])
    if stat in dictstat.keys():
        dictstat[stat] += 1
    else:
        dictstat[stat] = 1
    tcount += 1
    if tcount == 10:
        sortedme = sorted(dictstat.keys())
        print("File size:", tsize)
        for keys in sortedme:
            print("{}: {}".format(keys, dictstat[keys]))
        tcount = 0
        continue
