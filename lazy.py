
# helper function to print and return a value
pr = lambda s, i : print(s, i) or i

def source1(N):  # eager`evalution`
    result = []
    for i in range(N):
        result.append(pr('create1:', i))
    return result

def source2(N):  # lazy evaluation
    for i in range(N):
        yield pr('create2:', i)

def source3(N):  # eager: list comprehension
    return [pr('create3:', i) for i in range(N) ]

def source4(N):  # lazy: generator expression
    return (pr('create4:', i) for i in range(N) )

def sink(source):
    print('-----------------', source.__name__)
    for i in source(3):
        pr('consume:', i)

sink(source1)
sink(source2)
sink(source3)
sink(source4)
