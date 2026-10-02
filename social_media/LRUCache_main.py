import math
import LRUCache
from frozendict import frozendict

def main():
    for x in range(1, 6):
        print(f'square_root({x}):',square_root(x))
    for x in reversed(range(1, 6)):  # same input but reverse
        print(f'square_root({x}):',square_root(x))

def lru_cache(func):  # our own lru_cache decorator
    cache = LRUCache.LRUCache(3)  # only remember last 3
    def wrapper(*args, **kwargs):
        input = (args, frozendict(kwargs))  # make hashable
        output = cache.get(input)
        if output is None:
            output = func(*args, **kwargs)
        cache.put(input, output)
        return output
    return wrapper

@lru_cache  # use lru_cache decorator
def square_root(x):
    print(f'expensive: math.sqrt({x})')
    return math.sqrt(x) 

if __name__ == '__main__':
    main()
