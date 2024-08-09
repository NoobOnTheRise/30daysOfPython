"""
   List  - Ordered collection of items
           They store multiple items in a single variable.
           Can alter lists after creation.
"""

l = [3, 5, 6]
print(l)
print(type(l))
print(l[0])

# Alter list after creation
l[0] = 9
print(l)
print(l[-2])  # len(l) - 2 hence answer is 5

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

if "FYBScIT" in details:
   print("yes")
else:
   print("no")

#slicing
print(details[1:-1])
print(details[1:4:2])

marks = [1, 5, 7, 2, 4, 6, 8, 2, 2, 4, 6, 7, 1, 3]
print(marks[1:8])
print(
    marks[1:8:2]
)  # jump index - takes from 1 to 8 and jump the second index. Answer - [5,2,6,2]

lst = [i for i in range(4)]
print(lst)
lst1 = [i * i for i in range(10) if i % 2 == 0]
print(lst1)
