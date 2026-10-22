import random

def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K

n = 5
data = [random.randrange(n) for i in range(n)]
print(f'{data=}')

def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

data_sorted = sorted(data, key = cmp_to_key(mycmp))
print(f'{data_sorted=}')
