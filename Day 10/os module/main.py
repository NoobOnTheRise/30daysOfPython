# OS module - provides functions for interacting with the operating system
# It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

import os

if (not os.path.exists("data")):
    os.mkdir("data")
    for i in range(0, 10):
        os.mkdir(f"data/Day {i+1}")

folders = os.listdir("data")

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

# remove dir
os.rmdir("delete")

# remove file
os.remove("delete/delete.txt")
