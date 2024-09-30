#!/usr/bin/python3

# 1-safe_print_integer.py

def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Attempt to format and print the value as an integer
        return True
    except (ValueError, TypeError):
        return False
