# helper function to print and return a value
pr = lambda s, i : print(s, i) or i

def source1(n):  # eager evalution
    result = []
    for i in range(n):
        result.append(pr('create1:', i))
    return result

def source2(n):  # lazy evaluation
    for i in range(n):
        yield pr('create2:', i)  # yield instead of return

def source3(n):  # eager: list comprehension
    return [pr('create3:', i) for i in range(n)]

def source4(n):  # lazy: generator expression
    return (pr('create4:', i) for i in range(n))  # () instead of []

class MyIterator:
    def __init__(self, current, iterable):
        self.current = current
        self.iterable = iterable
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= len(self.iterable):
            raise StopIteration
        value = pr('create5:', self.current)
        self.current += 1
        return value

class Source5:  # lazy: iterable class
    def __init__(self, n):
        self.n = n
    def __len__(self):
        return self.n
    def __iter__(self):
        return MyIterator(0, self)


def sink(source):
    print('-----------------', source.__name__)
    for i in source(3):
        pr('consume:', i)

sink(source1)
sink(source2)
sink(source3)
sink(source4)
sink(Source5)
