# Docstrings - string literals that appear right after the definition of a function, method, class, or module.
# Docstrings vs comments - Docstrings are used to document a function, class, module, or method. Comments are used to add notes to the code


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)


square(5)
print(square.__doc__)

#pep-8 - guideline for writing python code. Python enhancement proposal.
