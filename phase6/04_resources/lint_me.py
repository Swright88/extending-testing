"""
This is a file for trying out Pylint
"""
import os

def open_foo_file():
    """
    Opens the 'foo.txt' file in the 'subdir' directory, reads its contents,
    and returns the lines as a list.

    Returns:
        list: The contents of the file as a list of strings.

    Raises:
        FileNotFoundError: If the 'foo.txt' file or 'subdir' directory is not found.
    """
    try:
        os.chdir("subdir")
        filedesc = open("foo.txt", "w", encoding="utf-8")
        contents = filedesc.readlines()
        filedesc.close()
    except FileNotFoundError:
        print("Couldn't find the file or directory")
        contents = None
    return contents

if __name__ == "__main__": # \r\n
    open_foo_file() # \r\nEOF
    