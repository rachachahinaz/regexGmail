import re

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}"
text = "becheriracha1@gamil.com"
text1 = "becheri@hhhh"

match = re.match(pattern, text)
match1 = re.match(pattern, text1)
b = bool(match)
b1 = bool(match1)
print(b)
print(b1)
