def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print()
