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
