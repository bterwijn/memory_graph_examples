# Python Cheat Sheet: Loops, If Conditions & Functions


# 1. For Loop

# Used to iterate over a sequence such as a list, tuple, string or range.
# Executes the block of code for each item in the sequence.

# Syntax:
# for variable in sequence:
#     statement(s)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# For Loop with If Condition

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")


# 2. While Loop

# Used to repeat a block of code as long as the condition is True.
# The condition is checked before each execution.

# Syntax:
# while condition:
#     statement(s)

count = 1

while count <= 5:
    print(count)
    count += 1


# While Loop with If Condition

num = 1

while num <= 10:
    if num % 2 == 0:
        print(num, "is even")
    num += 1


# 3. If Statements

# Used to make decisions based on conditions.

# Syntax:
# if condition:
#     statement(s)
# elif another_condition:
#     statement(s)
# else:
#     statement(s)

age = 20

if age < 18:
    print("Minor")
elif age == 18:
    print("Just 18!")
else:
    print("Adult")


# 4. Functions

# Used to group code into reusable blocks.
# Functions help improve organization and reusability.

# Syntax:
# def function_name(parameters):
#     statement(s)
#     return value  # Optional

def greet(name):
    message = "Hello, " + name + "!"
    return message


result = greet("Maheswari")
print(result)


# Functions with If and For

def even_numbers(nums):
    even_list = []

    for number in nums:
        if number % 2 == 0:
            even_list.append(number)

    return even_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_numbers(numbers)
print(result)


# Quick Notes

# A for loop is useful when the number of iterations is known.
# A while loop is useful when the number of iterations is unknown.
# if, elif and else are used for decision-making.
# Functions improve reusability and modularity.
# Use meaningful variable and function names.
# Proper indentation is important in Python.
