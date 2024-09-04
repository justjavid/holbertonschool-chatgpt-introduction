#!/usr/bin/python3
import sys

print("Script and arguments:")
for i in range(1, len(sys.argv)):  # Start from 1 to skip the script name
    print(f"Argument {i}: {sys.argv[i]}")

