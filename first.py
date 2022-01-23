#!/bin/python3

import sys
from datetime import datetime as dt

#Print String
print("Hello World")
print(sys.version)
print(dt.now())

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                        hello               "
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

# Lists []
# Dictionaries {}
# Tuples ()

grades = ("A", "B", "C")
print(grades[1:])

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8}
print(drinks)
