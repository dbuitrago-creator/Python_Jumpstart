"""
Examples to demonstrate more available string methods in python 3
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))

# Sub-Strings
# Starting index is inclusive
# Ending index is exclusive
# Will print out index in between 1 - 6
sub = a[1:6]
step =a[1:8:4]

print("****************")

print(sub)

print(step)

"""
More examples of string slicing and Indexing 
"""

# No starting or ending index it will print the whole string
b = "This is a string "
substring=b[:]
print(substring)

# Will print his is a string
c = "This is a string "
substring = c[1:]
print(substring)

# Will print g
d = "This is a string"
substring= d[-1:]
print(substring)

# Will print n
e = "This is a string"
substring = e[-2]
print(substring)

# To reverse the string
f ="This is a string"
substring = f[::-1]
print(substring)

