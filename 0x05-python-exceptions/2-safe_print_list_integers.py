#!/usr/bin/python3

# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    try:
        for i in range(x):
            try:
                # Attempt to format and print the element as an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                # Ignore non-integer elements
                continue
    except IndexError:
        # If x exceeds the list length, handle the out-of-range error
        pass
    print()  # Print a new line after the elements
    return count
