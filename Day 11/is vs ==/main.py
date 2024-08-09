# is =  exact location in memory comparison
# == = compare value

# strings and integers are immutable, which means that once they are created, their value cannot be changed
a = 4
b = "4"
print(a == b)
print(a is b)

c = [1,2,34]
d = [1,2,34]
print(c == d)
print(c is d)

e = 4
f = 4
print(e == f)
print(e is f)

g = None
h = None
print(g == h)
print(g is h)