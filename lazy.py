
# helper function to print when a value is created 
create = lambda i : print('create:', i) or i

def source1(N):  # eager`evalution`
    result = []
    for i in range(N):
        result.append(create(i))
    return result

def source2(N):  # lazy evaluation
    for i in range(N):
        yield create(i)

def source3(N):  # eager: list comprehension
    return [create(i) for i in range(N) ]

def source4(N):  # lazy: generator expression
    return (create(i) for i in range(N) )

def sink(source):
    print('-----------------', source.__name__)
    for i in source(3):
        print('consume:', i)

sink(source1)
sink(source2)
sink(source3)
sink(source4)
