#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        # Try to format the value as an integer using {:d}
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # If it fails, print an error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False
