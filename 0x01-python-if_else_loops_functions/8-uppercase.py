#!/usr/bin/python3
def uppercase(str):
    for indx in range(len(str)):
        chara = ord(str[indx])
        if chara >= 97 and chara <= 122:
            chara = chara - 32
        print("{}".format(chr(chara)), end="")
    print()
