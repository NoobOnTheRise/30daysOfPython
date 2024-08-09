# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called.
# Can simplify the code of a program by removing the need to manually cache the results of a function
# Can be achieved using the functools.lru_cache decorator.

import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n * 5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")
