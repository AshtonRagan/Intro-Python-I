"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
cut = slice(1, 2)
print(a[cut])

# Output the second-to-last element: 9
cut = slice(4, 5)
print(a[cut])

# Output the last three elements in the array: [7, 9, 6]
cut = slice(3, len(a))
print(a[cut])

# Output the two middle elements in the array: [1, 7]
cut = slice(2, 4)
print(a[cut])

# Output every element except the first one: [4, 1, 7, 9, 6]
cut = slice(1, len(a))
print(a[cut])

# Output every element except the last one: [2, 4, 1, 7, 9]
cut = slice((len(a)-1))
print(a[cut])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
cut = slice(7, 12)
print(s[cut])
