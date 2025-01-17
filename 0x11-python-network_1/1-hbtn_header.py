#!/usr/bin/python3
"""Fetches the X-Request-Id header from a given URL using urllib."""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
