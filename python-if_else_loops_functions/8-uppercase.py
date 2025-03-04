#!/usr/bin/python3


def uppercase(string):
    new_str = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            new_str += chr(ord(char) - 32)
        else:
            new_str += char
    print("{}".format(new_str))
