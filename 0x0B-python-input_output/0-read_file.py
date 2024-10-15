#!/usr/bin/python3
"""defining read_file function"""

def read_file(filename=""):
    """reads filename with utf-8"""
    with open(fielname, eencoding='utf-8') as f:
        print(f.read(), end="")
