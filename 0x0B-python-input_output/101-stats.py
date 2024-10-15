#!/usr/bin/python3
import sys

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
total_size = 0
count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        if len(parts) >= 6:
            total_size += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1

        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
