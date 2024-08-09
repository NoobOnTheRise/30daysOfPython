#Modes
# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).

f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

readTxt = open('myfile1.txt', 'w')
readTxt.write("Hello World")
readTxt.close()

makeFile = open('myfile2.txt', 'a')
makeFile.write("Hi")
makeFile.close()

f = open('myfile.txt', 'a')
f.write(" Hello ")
f.close()
#It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

# no need to close with the below code
with open('myfile.txt', 'a') as f:
    f.write(" Hello from inside ")
