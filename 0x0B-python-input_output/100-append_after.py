#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as file:
        content = file.readlines()
        file.seek(0)  # Go back to the start of the file
        for line in content:
            file.write(line)
            if search_string in line:
                file.write(new_string)
