# List Methods
print("---------sort----------")
marks = [1,2,4,5,6,7,3]
marks.append(67)
marks[4]=8
print("Before sort: ",marks)
marks.sort()
print("After sort (Ascending): ",marks)
marks.sort(reverse = True)
print("After sort (Desending): ",marks)

print("---------index----------")

print(marks.index(3))

print("---------count----------")

print(marks.count(4))

print("--------copy-----------")
copyOfMarks = marks.copy()
print(copyOfMarks)

print("--------insert-----------")
copyOfMarks.insert(2,788)
print(copyOfMarks)

print("---------extend----------")
m = [900,1000,1100]
marks.extend(m)
print(marks)

print("---------concatenate----------")
k = copyOfMarks + m
print(k)
