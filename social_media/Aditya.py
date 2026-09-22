# 1. Reverse a string
s = "hello"
print(s[::-1])

# 2. Check for a palindrome
def is_palindrome(s):
    return s == s[::-1]
print(f'{is_palindrome("abba")=}')

# 3. Count word frequency in a list
from collections import Counter

words = ['apple', 'banana', 'apple', 'apple']
print(f'{Counter(words)=}')

# 4. Find duplicate elements
lst = [1, 2, 3, 2, 4]
duplicates = {x for x in lst if lst.count(x) > 1}
print(f'{duplicates=}')

# 5. Fibonacci using recursion
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)
print(f'{fib(3)=}')

# 7. Check if a list is sorted
def is_sorted(lst):
    return lst == sorted(lst)
print(f'{is_sorted([1, 2, 3])=}')

# 8. Flatten a nested list (heading corrected)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(f'{flat=}')

# 9. Square numbers using map (heading corrected)
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))
print(f'{squares=}')

# 10. Lambda and map usage (duplicates number 9)
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))
print(f'{squares=}')
