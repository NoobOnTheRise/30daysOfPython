a ="Harry"
print(len(a))
# Creates a new string when using the following since strings are immutable
print(a.upper()) 
print(a.lower())
b ="!!!!!!Minal!!!!!!!"
print(b.rstrip("!"))
print(b.lstrip("!"))
print(b.replace("Minal","Mini"))
print(b.split("!")) # converts to a list
c= "introduction tO pYthon"
print(c.capitalize()) # converts first letter to capital and rest to small
print(c.center(50)) # adds spaces to the string
print(c.count("i")) # returns the number of times the given value.

str ="Welcome to the console !!!!"
print(str.endswith("!"))
print(str.find("t")) # gives the first occurance of the given value

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

str2 = "Welcome"
print(str2.isalpha())  # returns True only if the entire string only consists of A-Z, a-z.

str3 = "WelcomeToTheConsole"
print(str3.isalnum()) # returns True only if the entire string only consists of A-Z, a-z, 0-9.

d = "HEY"
e = "hey"
print(e.islower()) # returns True if all the characters in the string are lower case
print(d.isupper())# returns True if all the characters in the string are upper case

value = "We wish you a Merry Christmas"
print(value.isprintable()) # returns True if all the values within the given string are printable, if not, then return False
# non printable characters : /n, /t 


Spacebar = "        "       #using Spacebar
print(Spacebar.isspace())
Tab = "        "       #using Tab
print(Tab.isspace())

titleex = "World Health Organization" 
print(titleex.istitle()) #True only if the first letter of each word of the string is capitalized

print(titleex.startswith("Python"))
print(titleex.startswith("World"))
print(str1.swapcase())
# Upper case are converted to lower case and lower case to upper case.

example = "he's name is Dan. Dan is an honest man."
print(example.title()) # capitalizes each letter of the word within the string.

