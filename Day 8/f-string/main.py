letter = "Hey my name is {1} and I am from {0}"
country = "Sri Lanka"
name = "Minal"

print(letter.format(name, country))

# f-strings - Literal String Interpolation. 
# The primary focus of this mechanism is to make the interpolation easier.

print(f"Hey my name is {name} and I am from {country}")

price = 20
txt = f"Price only {price:.2f} dollers!"
print(txt)
print(f"{2 * 30}") 
