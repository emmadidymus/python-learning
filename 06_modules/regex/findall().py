"""
It returns a list with all the matches, in the order they are found
It returns an empty list if no matches are found.
"""

import re

x = ("The rain in Spain")

print(re.findall("ai", x))


import re

x = ("The rain in Spain")

print(re.findall("go", x))