# Python Basics - Memory Graph Web Debugger

print("=== 1. Python Syntax and Indentation Rules")

# Correct indentation defines a code block.
if 5 > 2:
    print("Five is greater")
    print("than two")

# Incorrect indentation would raise IndentationError:
# if 5 > 2:
# print("Five is greater")


print("\n=== 2. Variables and Constants")

# Variables store references to values.
name = "Python"
age = 25
is_student = True

print(f"{name=}")
print(f"{age=}")
print(f"{is_student=}")

# Constants are uppercase by convention.
# Python does not enforce constant values.
PI = 3.14159
MAX_SIZE = 100

print(f"{PI=}")
print(f"{MAX_SIZE=}")


print("\n=== 3. Data Types in Python")

print("\n--- Numeric Types: int, float, complex")

a = 10
b = 3.14
c = 2 + 3j

print(f"{a=}, {type(a)=}")
print(f"{b=}, {type(b)=}")
print(f"{c=}, {type(c)=}")


print("\n--- Text Type: str")

text = "Hello"

print(f"{text=}")
print(f"{type(text)=}")


print("\n--- Sequence Types: list, tuple, range")

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_range = range(1, 5)

print(f"{my_list=}")
print(f"{my_tuple=}")
print(f"{list(my_range)=}")

print(f"{type(my_list)=}")
print(f"{type(my_tuple)=}")
print(f"{type(my_range)=}")


print("\n--- Set Types: set, frozenset")

my_set = {1, 2, 3}
my_frozenset = frozenset({1, 2, 3})

print(f"{my_set=}")
print(f"{my_frozenset=}")
print(f"{type(my_set)=}")
print(f"{type(my_frozenset)=}")


print("\n--- Mapping Type: dict")

my_dict = {
    "name": "Alice",
    "age": 25
}

print(f"{my_dict=}")
print(f"{type(my_dict)=}")


print("\n=== 4. Type Casting and Type Checking")

print("\n--- Type Casting")

num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"{num_str=}")
print(f"{num_int=}")
print(f"{num_float=}")

print(f"{type(num_int)=}")
print(f"{type(num_float)=}")


print("\n--- Type Checking")

x = 10

print(f"{type(x)=}")
print(f"{isinstance(x, int)=}")
print(f"{isinstance(x, float)=}")


print("\n=== 5. Taking User Input")

# Normally:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# Predefined inputs for automatic execution.
user_name = "Heena"
user_age_text = "22"

# input() always returns a string.
print(f"{user_name=}")
print(f"{user_age_text=}")

user_age = int(user_age_text)

print(f"Hello {user_name}!")
print(f"You are {user_age} years old.")

print(f"{type(user_age_text)=}")
print(f"{type(user_age)=}")


print("\n=== 6. Printing Output")

print("\n--- Basic print()")

print("Hello, Python!")


print("\n--- F-strings")

name = "Alice"
age = 25

print(f"Name: {name}, Age: {age}")


print("\n--- format() Method")

name = "Bob"
score = 95

print("Name: {}, Score: {}".format(name, score))


print("\n=== 7. Comments in Python")

# This is a single-line comment.
print("Hello")

# Comments are ignored by Python.

"""
This is a multi-line string.
It can span multiple lines.

Triple-quoted strings are often used
for documentation (docstrings).
They are not technically comments.
"""

print("Hello")


print("\n=== End of Python Basics ===")
