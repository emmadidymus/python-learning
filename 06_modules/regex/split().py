"""
split() returns a list where the string has been split at each match
"""

import re

x = ("The rain in Spain")

print(re.split("\\s", x, 2))