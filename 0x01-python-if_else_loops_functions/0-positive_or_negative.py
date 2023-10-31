#!/usr/bin/python3
import random
number = random.randint(-10, 10)
s1 = " is positive"
s2 = " is zero"
s3 = " is negative"
if number > 0:
    print("{}".format(number) + s1)
elif number == 0:
    print("{}".format(number) + s2)
else:
    print("{}".format(number) + s3)
