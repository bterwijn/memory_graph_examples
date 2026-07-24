# Python Basics

# This is a comment
print("Hello, World!")


# Variables & Data Types
x = 10              # int
y = 10.5            # float
name = "Alex"       # string
is_active = True    # boolean

print(x)
print(y)
print(name)
print(is_active)


# Type Checking & Conversion
print(type(x))
print(int("10"))
print(float("10.5"))
print(str(100))


# Input & Output
name = input("Enter your name: ")
print("Hello", name)


# Strings
text = "Python"

print(text.upper())
print(text.lower())
print(text[0])
print(text[0:3])
print(len(text))


# Lists
nums = [1, 2, 3]
print(nums)

nums.append(4)
print(nums)

nums.remove(2)
print(nums)

print(nums[0])


# Tuples (Immutable)
data = (1, 2, 3)
print(data)
print(data[0])


# Sets
items = {1, 2, 3}
print(items)

items.add(4)
print(items)

items.remove(2)
print(items)


# Dictionaries
user = {"name": "Alex", "age": 25}

print(user)
print(user["name"])
print(user.keys())
print(user.values())


# Operators

# Arithmetic
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10**3)

# Comparison
print(10 == 3)
print(10 != 3)
print(10 > 3)
print(10 < 3)
print(10 >= 3)
print(10 <= 3)

# Logical
print(True and False)
print(True or False)
print(not True)


# Conditional Statements
x = 10

if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")


# Loops

# For Loop
for i in range(5):
    print(i)

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1


# Functions
def greet(name):
    return "Hello " + name


print(greet("Alex"))


# Lambda Functions
add = lambda a, b: a + b

print(add(2, 3))


# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)


# Exception Handling
try:
    x = int("abc")
except ValueError:
    print("Error occurred")
finally:
    print("Done")


# File Handling
with open("data.txt", "w") as file:
    file.write("Hello from Python!")

with open("data.txt", "r") as file:
    content = file.read()

print(content)


# Importing Modules
import math

print(math.sqrt(16))

from math import sqrt

print(sqrt(25))


# Useful Built-in Functions
numbers = [3, 1, 4, 2]

print(len(numbers))
print(type(numbers))
print(list(range(5)))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))


# Python Best Practices (Beginner)

# Use meaningful variable names.
# Follow indentation strictly.
# Write reusable functions.
# Handle errors properly.
