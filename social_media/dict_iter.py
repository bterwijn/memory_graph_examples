# Dictionary key-value iteration in Python

# Method 1 - Iterate through keys
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

for key in student:
    print(key)


# Method 2 - Using items()
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)


# Method 3 - Using keys() and values()
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)


# Method 4 - Taking user dictionary
data = {"city": "Delhi", "country": "India"}

for key, value in data.items():
    print(f"{key} : {value}")
