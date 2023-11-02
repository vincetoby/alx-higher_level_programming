#!/usr/bin/python3
def fib(n):
    a, b = 0, 1
    while a < n:
        print("{} ".format(a), end="")
        a, b = b, a + b
    print()

def fib2(n):
    str = "hello you bitch"
    a = 0
    while a < n:
        print("{}".format(str))
        a = a + 1
    print()
