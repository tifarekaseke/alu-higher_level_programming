#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = str[39:66] + str[107:113] + str[:6]  # Correct slices for the required output
print(str)
