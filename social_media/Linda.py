print("# 01 Swap Two Variables")
a = 10
b = 20
a, b = b, a
print(a, b)

print("# 02 Check Even or Odd")
n = 7
result = "Even" if n % 2 == 0 else "Odd"
print(result)

print("# 03 Reverse a String")
text = "python"
print(text[::-1])

print("# 04 Convert List to Uppercase")
words = ["python", "sql", "ai"]
result = [x.upper() for x in words]
print(result)

print("# 05 Remove Duplicates")
numbers = [1, 2, 2, 3, 3, 4]
unique = list(set(numbers))
print(unique)

print("# 06 Find Maximum Value")
numbers = [10, 25, 7, 40]
print(max(numbers))

print("# 07 Find Minimum Value")
numbers = [10, 25, 7, 40]
print(min(numbers))

print("# 08 Square Every Number")
numbers = [1, 2, 3, 4]
result = [x**2 for x in numbers]
print(result)

print("# 09 Get Only Even Numbers")
numbers = [1, 2, 3, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

print("# 10 Get Only Odd Numbers")
numbers = [1, 2, 3, 4, 6]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

print("# 11 Find List Length")
languages = ["Python", "SQL", "Java"]
print(len(languages))

print("# 12 Check If an Item Exists")
languages = ["Python", "SQL", "Java"]
print("Python" in languages)

print("# 13 Create a List of Numbers")
print(list(range(1, 11)))

print("# 14 Join a List of Strings")
names = ["Alice", "Bob", "Rahul"]
result = "-".join(names)
print(result)

print("# 15 Count Occurrences")
numbers = [5, 2, 5, 3, 5, 9]
print(numbers.count(5))
