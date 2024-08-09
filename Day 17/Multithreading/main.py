# Multithreading
from concurrent import futures
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
  print(f'sleeping for {seconds} seconds')
  time.sleep(seconds)

# threads
def main():
  # tp1 = time.perf_counter()
  # # normal code
  # func(4)
  # func(2)
  # func(1)
  # tp2 = time.perf_counter()
  # print(tp2 - tp1)
  tp3 = time.perf_counter()
  t1 = threading.Thread(target=func,args=[4])
  t2 = threading.Thread(target=func,args=[2])
  t3 = threading.Thread(target=func,args=[1])
  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()

  tp4 = time.perf_counter()
  print(tp4 - tp3)

def PoolingDemo(): # parallel execution
    with ThreadPoolExecutor() as executor:
   #   future1 = executor.submit(func,3)
   #   print(future1.result())
   #   future2 = executor.submit(func,2)
   #   print(future2.result())
   #   future3 = executor.submit(func,5)
   #   print(future3.result())
      l = [3,5,1,2]
      results = executor.map(func, l)
      for result in results:
        print(result)


PoolingDemo()