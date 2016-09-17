import re

string = "Many applications use Python as an embedded scripting language."

# Return all words beginning with character 'a', as a list of strings
print re.findall(r"\ba[\w]*", string)
# ['applications', 'as', 'an']

# Return all words beginning with character 'a', as an iterator yielding match objects
_iter = re.finditer(r"\ba[\w]*", string)
for match in _iter:
    print "'{g}' was found between the indices {s}".format(g=match.group(), s=match.span())
# 'as' was found between the indices (29, 31)
# 'an' was found between the indices (32, 34)

# Split string by any character which is not a UNICODE word character
print re.split("\W+", string)
# ['Many', 'applications', 'use', 'Python', 'as', 'an', 'embedded', 'scripting', 'language', '']

# Split string by any character which is not a UNICODE word character at most 2 split
print re.split("\W+", string, 2)
# ['Many', 'applications', 'use Python as an embedded scripting language.']

# Split string by any character which is not a UNICODE word character at most 3 split
print re.split("\W+", string, 3)
# ['Many', 'applications', 'use', 'Python as an embedded scripting language.']

# Split string by any character which is not a UNICODE word character at most 4 split
print re.split("\W+", string, 4)
# ['Many', 'applications', 'use', 'Python', 'as an embedded scripting language.']

# If the splitting pattern does not occur in the string,
# string is returned as the first element of the list
print re.split("(:)", string)
# ['Many applications use Python as an embedded scripting language.']

# Replace all occurrences of space, comma, or dot with colon
print re.sub("[ ,.]", ":", string)
# Many:applications:use:Python:as:an:embedded:scripting:language:

# Replace maximum 2 occurences of pattern
print re.sub("[ ,.]", ":", string, 2)
# Many:applications:use Python as an embedded scripting language.

# Replace as 'sub', but return a tuple of (new string, number of replacements)
print re.subn("[ ,.]", ":", string)
