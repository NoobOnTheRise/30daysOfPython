"""
There are four types of arguments that we can provide in a function:
1.Default Arguments
"""
def avg(a=9,b=1):
  print("The average is :", (a+b)/2)

avg(1,3)
avg()

# 2.Keyword Arguments - Can change order of the args

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
name(lname = "Potter", mname = "Albus", fname = "Harry")

# 3. Variable length Arguments

def averge(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  return sum/len(numbers)

c = averge(5,6,7,1)
print(c)

# 4. Required Arguments - Must have all args

def printName(fname, mname, lname="Egg"):
    print("Hello,", fname, mname, lname)

printName("Peter", "Quill")