import collections as cl

def main():
    chainmap_example()
    counter_example()

def chainmap_example():
    d1 = {'a': 'aaa', 'b': 'bbb'}
    d2 = {1: 111, 2: 222}
    chainmap = cl.ChainMap(d1, d2)

    print(chainmap['a'])

    chainmap[3] = 333
    chainmap |= {'c': 'ccc'}

    child = chainmap.new_child( {4: 444} )
    parents = child.parents
    del d1, d2, chainmap, child, parents  # cleanup

def counter_example():
    counter = cl.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
    print(counter)
    print(counter['a'])

    elements = counter.elements()
    print(list(elements))
    print(counter.most_common(2))
    counter.subtract(['b', 'c', 'c'])
    print(counter)
    print(counter.total())
    del counter, elements  # cleanup

if __name__ == '__main__':
    main()
