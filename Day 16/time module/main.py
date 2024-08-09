# The Time Module - provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

import time

t = time.time()  #  current time as a floating-point number
print(t)

print("Start:", time.time())
time.sleep(
    2
)  #  suspends the execution of the current thread for a specified number of seconds
print("End:", time.time())

t1 = time.localtime(
)  # formats a time value as a string, based on a specified format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t1)
print(formatted_time)
