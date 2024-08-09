 # Generators - special type of functions that allow you to create an iterable sequence of values.
# Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
# you can create a generator by using the yield statement in a function

def my_generator():
  for i in range(5):
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
  print(i)

#  main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
# the values are generated only when they are requested
# This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front