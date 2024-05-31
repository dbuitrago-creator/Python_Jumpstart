"""
Examples to show available string methods in python
"""

# Accessing characters in a string
# Index starts from zero

# Will print out y
first = "nyc" [0]
print(first)

# Will print out s
city = "sfo"
ft = city[0]
print(ft)

"""
len()
lower()
upper()
str()
"""
example = "this Is a Mixed Case"

# Will print out the string in all lowercase
print(example.lower())

# Will print out the string in all uppercase
print(example.upper())

# Will print out the length of the string
print(example.__len__())

# Concatenates the string "this Is a Mixed Case" with the string representation of the integer '2'
print(example + " " + str(2))


# Convert a float to a string
float_num = 3.14
str_float = str(float_num)
print(str_float)

# Convert a boolean to a string
boolean_value = True
str_boolean = str(boolean_value)
print(str_boolean)

"""
Concatenation 
Demonstrate how to concatenate in python 3 
"""
print("Hello " + " " + " World !!!")
print( first + "" + city)
