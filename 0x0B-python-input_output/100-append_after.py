#!/usr/bin/python3
"""Write a function that inserts a line of text to a file, after each
   line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """Function to add a new string when finished the line if the
       search_string if find in the current line"""
    with open(filename, 'r') as f:
        new_file_lines = []
        for line in f:
            new_file_lines.append(line)
            if line.find(search_string) != -1:
                new_file_lines.append(new_string)
    with open(filename, 'w') as f:
            f.writelines(new_file_lines)
