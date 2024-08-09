f = open('myfile.txt', 'r')
while True:
  line = f.readline()
  if not line:
    break
  print(line)
f.close()

f = open('myfile1.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
  f.write(line + '\n')
f.close()
