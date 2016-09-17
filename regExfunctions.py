import re

string = "Many applications use Python as an embedded scripting language."

# Return all words beginning with character 'a', as a list of strings
print re.findall(r"\ba[\w]*", string)
# ['applications', 'as', 'an']
