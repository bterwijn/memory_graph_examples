from collections import Counter

elements = ['a', 'b', 'c', 'a', 'b', 'a']
print(f'{elements=}')

print('\n=== count the elements')
counter = Counter(elements)
print(f'{counter=}')

print('\n=== print count of an element')
print(f'{counter['a']=}')
print('Missing elements have count 0 instead of raising KeyError')
print(f'{counter['z']=}')

print('\n=== find the two most common elements')
print(f'{counter.most_common(2)=}')

print('\n=== update() adds to existing counts')
counter.update(['a', 'd', 'd'])
print(f'{counter=}')
counter.update({'a': -1, 'd':2})
print(f'{counter=}')

print('\n=== subtract() decounts; zeros and negatives are retained')
counter.subtract(['b', 'b', 'c', 'c'])
print(f'{counter=}')

print('\n=== total() gives the sum of all counts')
print(f'{counter.total()=}')

print('\n=== elements() gives positive-count elements in order of first encounter')
elements = counter.elements()
print(f'{type(elements)=}')
print(f'{list(elements)=}')

print('\n=== unary plus removes zero and negative counts')
print('=== unary minus keeps only negative counts, as positive')
print(f'{ counter=}')
print(f'{+counter=}')
print(f'{-counter=}')

print('\n=== operations on two counters')
left  = Counter(a=3,      b=1, d= 1, e= 3, f= 5, g=-5)
right = Counter(a=1, c=2,      d=-2, e=-3, f=-4, g=-6, h=-7)
# in order of counts:
print(f'{left | right=}')  # union, maximum of counts, only positive elements
print(f'{left & right=}')  # intersection, minimum of counts, only positive elements
print(f'{left + right=}')  # addition, add the counts, only positive elements
print(f'{left - right=}')  # subtraction, subtract the counts, only positive elements

print('\n=== comparison of two counters')
left  = Counter(a=1,      b=0)
right = Counter(a=1, c=0,    )
print(f'{left=} {right=}')
print(f'{left == right}')  # True if all counts agree, missing counts are treated as zero
print(f'{left <= right}')  # True if all counts in 'left' are a subset of those in 'right'
print(f'{left <  right}')  # True if all counts in 'left' are a proper subset of those in 'right'
print(f'{left >= right}')  # True if all counts in 'left' are a superset of those in 'right'
print(f'{left >  right}')  # True if all counts in 'left' are a proper superset of those in 'right'

print('\n=== comparison of two counters')
left  = Counter(a=1,      b=1)
right = Counter(a=1, c=0,    )
print(f'{left=} {right=}')
print(f'{left == right}')  # True if all counts agree, missing counts are treated as zero
print(f'{left <= right}')  # True if all counts in 'left' are a subset of those in 'right'
print(f'{left <  right}')  # True if all counts in 'left' are a proper subset of those in 'right'
print(f'{left >= right}')  # True if all counts in 'left' are a superset of those in 'right'
print(f'{left >  right}')  # True if all counts in 'left' are a proper superset of those in 'right'

print('\n=== missing keys versus stored zero counts')
counter = Counter(a=2, b=0)
print(f'{counter=}')
print(f'{counter["b"]=}')
print(f'{counter["z"]=}')
print(f'{"b" in counter=}')
print(f'{"z" in counter=}')

print('\n=== subtract() retains non-positive counts, the - operator discards them')
left = Counter(a=2, b=1)
right = Counter(a=3, b=1)
left_copy = left.copy()
left_copy.subtract(right)
print(f'{left_copy=}')
print(f'{left - right=}')
