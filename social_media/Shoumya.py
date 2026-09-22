print("# Python Basics")
# This is a comment
print("Hello, World!")

print("# Variables & Data Types")
x = 10            # int
y = 10.5          # float
name = "Alex"     # string
is_active = True  # boolean

print("# Type Checking & Conversion")
type(x)
int("10")
float("10.5")
str(100)

print("# Input & Output")
name = input("Enter your name: ")
print("Hello", name)

print("# Strings")
text = "Python"
text.upper()
text.lower()
text[0]
text[0:3]
len(text)

print("# Lists")
nums = [1, 2, 3]
nums.append(4)
nums.remove(2)
nums[0]

print("# Tuples (Immutable)")
data = (1, 2, 3)
data[0]

print("# Sets")
items = {1, 2, 3}
items.add(4)
items.remove(2)

print("# Dictionaries")
user = {"name": "Alex", "age": 25}
user["name"]
user.keys()
user.values()

print("# Operators")
# Arithmetic: +, -, *, /, %, **
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not

print("# Conditional Statements")
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")

print("# Loops")
# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

print("# Functions")
def greet(name):
    return "Hello" + name

print("# Lambda Functions")
add = lambda a, b: a + b

print("# List Comprehension")
squares = [x * x for x in range(5)]

print("# Exception Handling")
try:
    x = int("abc")
except ValueError:
    print("Error occurred")
finally:
    print("Done")

print("# File Handling")
# Requires an existing data.txt file.
with open("data.txt", "w") as f:
    f.write("Hello\nWorld\n!!!")
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

print("# Importing Modules")
import math
math.sqrt(16)

from math import sqrt
sqrt(25)

print("# Useful Built-in Functions")
# Example arguments added to make these calls valid.
len(nums)
type(nums)
range(5)
max(nums)
min(nums)
sum(nums)
sorted(nums)

print("# Python Best Practices (Beginner)")
# Use meaningful variable names.
# Follow indentation strictly.
# Write reusable functions.
# Handle errors properly.
