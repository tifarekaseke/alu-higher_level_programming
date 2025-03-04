#!/usr/bin/python3

import sys

args = sys.argv[1:]
count = len(args)

if count == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(count, "s" if count > 1 else ""))
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
