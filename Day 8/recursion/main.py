# Recursion is the process of defining something in terms of itself.
# factorial(7) = 7*6*5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1
# facorial(n) = n * factorial(n-1)
def facorial(n):
    if (n == 0 or n ==1):
     return 1
    else:
     return n * facorial(n-1)

print(facorial(3))
print(facorial(4))
print(facorial(5))

# Quiz -  Fibonacci series
# f1 = 0
# f2 = 1
# f3 = f1 + f2
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
  if n <= 1:
    return n
  else: 
    return fibonacci(n-1) + fibonacci(n-2)

num = input("Enter the range: ")
for i in range(int(num)):  
  print(fibonacci(i))
