#!/usr/bin/env python3
import argparse
import random
import string

# Create argument parser.
parser = argparse.ArgumentParser()
parser.add_argument("--letters", default = string.ascii_letters)
parser.add_argument("--digits", default = string.digits)
parser.add_argument("--punctuation", default = string.punctuation)
parser.add_argument("--length", type = int, default = 24)
parser.add_argument("--count", type = int, default = 10)
parser.add_argument("--silent", action = "store_true", default = False)

# Get arguments.
arguments = parser.parse_args()
letters = arguments.letters
digits = arguments.digits
punctuation = arguments.punctuation
length = arguments.length
count = arguments.count
silent = arguments.silent

# Check the silence.
if not silent:
    # Print arguments.
    print(f"Letters:     {letters}")
    print(f"Digits:      {digits}")
    print(f"Punctuation: {punctuation}")
    print(f"Length:      {length}")
    print(f"Count:       {count}")
    print()

# Generate passwords.
for _ in range(count):
    # Concatenate characters.
    characters = list(letters + digits + punctuation)
    # Shuffle characters.
    random.shuffle(characters)
    # Pick random characters.
    choices = random.choices(characters, k = length)
    # Join password.
    password = "".join(choices)
    # Print password.
    print(password)
