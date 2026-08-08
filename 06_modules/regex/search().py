"""
search() searches a string for a match and returns Match object if there is a match
"""

import re

x = ("The rain in Spain")

print(re.search("^The.*Spain$", x))