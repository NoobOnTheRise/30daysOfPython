"""
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
"""

# import time
import time

timestamp = time.strftime('%H:%M:%S')
print("Time now : " ,timestamp)
timestamp = int(time.strftime('%H'))
timestamp = int(input())

if (timestamp >= 0 and timestamp < 12) :
  print("Good Morning")
elif (timestamp >= 12 and timestamp < 18) :
  print("Good Afternoon")
else :
  print("Good Evening")