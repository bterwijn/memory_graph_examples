from collections import Counter
from pathlib import Path

print("=== 1. Swap two values ===")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Before: {a=}, {b=}")

a, b = b, a
print(f"After:  {a=}, {b=}")


print("\n=== 2. Reverse a list or string ===")
text = "Python"
backwards = text[::-1]
print(f"{text=}, {backwards=}")

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(f"{numbers=}, {reversed_numbers=}")


print("\n=== 3. Find the most common items ===")
words = ["apple", "banana", "apple", "cherry",
         "banana", "apple", "orange"]

counter = Counter(words)
common = counter.most_common(3)
print(f"{counter=}")
print(f"{common=}")


print("\n=== 4. Remove duplicates, keep the order ===")
items = ["a", "b", "a", "c", "b", "d", "a"]
unique = list(dict.fromkeys(items))
print(f"{items=}")
print(f"{unique=}")


print("\n=== 5. Merge two dictionaries ===")
defaults = {"theme": "light", "font_size": 12, "language": "en"}
user_prefs = {"theme": "dark", "font_size": 16}

settings = defaults | user_prefs
print(f"{defaults=}")
print(f"{user_prefs=}")
print(f"{settings=}")


print("\n=== 6. Read a file into lines ===")
Path("data.txt").write_text("Alice\nBob\nCharlie\n")
lines = Path("data.txt").read_text().splitlines()
print(f"{lines=}")


print("\n=== 7. Flatten a list of lists ===")
rows = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat = [x for row in rows for x in row]
print(f"{rows=}")
print(f"{flat=}")
