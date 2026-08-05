"""
Sorting a list of tuples by the second element
"""

students = [("Lima", 22), ("Tobias", 24), ("Red", 43), ("Jon", 32), ("Moi", 45)]

sorted_students = sorted(students, key = lambda x:x[1])
print(sorted_students)


"""
Sorting strings by length
"""

words = ["apple", "pie", "orange", "pomegranate", "peach"]

sorted_words = sorted(words, key=lambda x : len(x))
print(sorted_words)
