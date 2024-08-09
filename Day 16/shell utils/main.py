# Shutil is a Python module that provides a higher level interface for working with file and directories
# provides a convenient and efficient way to automate tasks that are commonly performed on files and directories

import shutil

# Copying a file
shutil.copy("src.txt", "dst.txt")

# Copying a directory
shutil.copytree("Day 16", "Day 17")

# Moving a file
shutil.move("src.txt", "dst.txt")

# Deleting a directory
shutil.rmtree("dir")