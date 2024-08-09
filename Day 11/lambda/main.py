# Lambda function - small anonymous function without a name

# Function to double the input
def double(x):
  return x * 2

print(double(5))
# Lambda function to double the input
doubleLambdaFunc = lambda x: x * 2
print(doubleLambdaFunc(5))

cube = lambda x: x * x * x
print(cube(5))

add = lambda x, y: x + y
print(add(4, 5))

k = lambda x, y: print(f'{x} * {y} = {x * y}')
k(3, 4)

def apply(func, value):
  return 6 + func(value)

print(apply(cube, 2))