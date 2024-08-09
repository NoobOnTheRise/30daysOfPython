# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. T
class Vector:

  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


v = Vector(2, 3, 4)
print(v)

v1 = Vector(3, 2, 4)
print(v1)

print(v + v1)
print(type(v + v1))
