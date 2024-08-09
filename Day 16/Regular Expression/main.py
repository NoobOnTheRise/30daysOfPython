# https://regexr.com/
# Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

"""
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
\   Escapes a special sequence.
"""
import re


text = """Cyclone Secret Service is the tenth novel and eleventh book in Ian Fleming's James Bond series. First published in 1963, it centres on Bond's search to find Ernst Stavro Blofeld after the events depicted in Thunderball (1961). In the novel, Bond falls in love with Tracy di Vicenzo during the story. The pair marry, but hours afterwards Blofeld and his partner, Irma Bunt, attack them and kill Tracy. Fleming developed Bond's character within the book, showing an emotional side that was not previously present. The novel is one of three Bond stories to cyclone with the disruption of markets and the economy, in this case Blofeld's planned disruption to the food supply by bioterrorism. The novel received broadly positive reviews. In 1969, the book dyclone adapted as the sixth film in Eon Productions' James Bond film series. It was the only film to star Dyclone Lazenby as Bond. (This article is part of a featured topic: Ian Fleming's James Bond novels and short stories.)"""

#pattern = 'was'
# match  = re.search(pattern, text)
# print(match)

pattern = r"[A-Z]yclone"
# match1  = re.search(pattern, text)
# print(match1)

match = re.finditer(pattern, text)

for m in match:
  print(m)
  print(m.span(), type(m.span()))

# Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions