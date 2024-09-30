#!/usr/bin/python3

# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()  # To ensure the new line after printing all elements
    return count
