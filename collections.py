import collections as cl


def main():
    chainmap_example()
    counter_example()
    deque_example()
    defaultdict_example()
    namedtuple_example()
    ordereddict_example()
    userdict_example()
    userlist_example()
    userstring_example()


def chainmap_example():
    print('\n=== ChainMap: one view of multiple dictionaries ===')
    d1 = {'a': 'aaa', 'b': 'bbb'}
    d2 = {'b': 'SECOND b', 1: 111, 2: 222}
    chainmap = cl.ChainMap(d1, d2)
    print(f'{chainmap=}')
    print('Lookups use the first dictionary containing the key')
    print(f"{chainmap['b']=}")
    print(f'{chainmap.maps=}')

    print('Writes and deletions affect only the first dictionary')
    chainmap[3] = 333
    chainmap |= {'c': 'ccc'}
    print(f'{d1=}')
    print(f'{d2=}')

    print('Changes to the original dictionaries are visible through the ChainMap')
    d2[1] = 999
    print(f'{chainmap[1]=}')

    print('Prepend a new mapping with new_child()')
    child = chainmap.new_child({4: 444, 'a': 'child a'})
    print(f'{child=}')
    print(f"{child['a']=}")
    print(f"{chainmap['a']=}")

    print('parents gives a ChainMap without the first mapping')
    parents = child.parents
    print(f'{parents=}')
    print(f'{list(child.keys())=}')


def counter_example():
    print('\n=== Counter: count hashable elements ===')
    counter = cl.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
    print(f'{counter=}')
    print(f"{counter['a']=}")
    print('Missing elements have count 0 instead of raising KeyError')
    print(f"{counter['z']=}")

    print('elements() repeats positive-count elements')
    elements = counter.elements()
    print(f'{list(elements)=}')

    print('Find the two most common elements')
    print(f'{counter.most_common(2)=}')

    print('Update adds to existing counts')
    counter.update(['a', 'd', 'd'])
    print(f'{counter=}')

    print('Subtract counts; zeros and negatives are retained')
    counter.subtract(['b', 'c', 'c'])
    print(f'{counter=}')
    print(f'{counter.total()=}')

    print('Multiset union (max), intersection (min), sum, difference')
    left = cl.Counter(a=3, b=1)
    right = cl.Counter(a=1, c=2)
    print(f'{left | right=}')
    print(f'{left & right=}')
    print(f'{left + right=}')
    print(f'{left - right=}')
    print('Unary plus removes zero and negative counts')
    print(f'{+counter=}')


def deque_example():
    print('\n=== deque: efficient operations at both ends ===')
    queue = cl.deque(['b', 'c'])
    print(f'{queue=}')
    print('Append to the right and left')
    queue.append('d')
    queue.appendleft('a')
    print(f'{queue=}')

    print('Pop from the left (FIFO queue)')
    first = queue.popleft()
    print(f'{first=}, {queue=}')
    print('Pop from the right (stack)')
    last = queue.pop()
    print(f'{last=}, {queue=}')

    print('Add several elements at both ends')
    queue.extend(['d', 'e'])
    queue.extendleft(['b', 'a'])  # each item is inserted on the left
    print(f'{queue=}')

    print('Rotate one position to the right')
    queue.rotate(1)
    print(f'{queue=}')
    print('Rotate two positions to the left')
    queue.rotate(-2)
    print(f'{queue=}')

    print('Bounded deque automatically discards opposite-end items')
    recent = cl.deque(maxlen=3)
    for value in [10, 20, 30, 40]:
        recent.append(value)
    print(f'{recent=}')


def defaultdict_example():
    print('\n=== defaultdict: supply a value for missing keys ===')
    groups = cl.defaultdict(list)
    print('First access to a missing key creates an empty list')
    for name, category in [('apple', 'fruit'), ('carrot', 'vegetable'),
                           ('pear', 'fruit')]:
        groups[category].append(name)
    print(f'{dict(groups)=}')
    print(f'{groups.default_factory=}')

    print('Count words with defaultdict(int)')
    counts = cl.defaultdict(int)
    for word in ['cat', 'dog', 'cat']:
        counts[word] += 1
    print(f'{dict(counts)=}')

    print('get() does not call the factory for a missing key')
    print(f"{groups.get('unknown')=}")
    print(f"{'unknown' in groups=}")
    print('Indexing a missing key does call the factory')
    print(f"{groups['unknown']=}")
    print(f"{'unknown' in groups=}")

    print('Use a custom factory for missing values')
    settings = cl.defaultdict(lambda: 'not specified')
    print(f"{settings['theme']=}")


def namedtuple_example():
    print('\n=== namedtuple: tuple with named fields ===')
    Point = cl.namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(f'{p=}')
    print('Access fields by position or name')
    print(f'{p[0]=}, {p.x=}, {p.y=}')
    print('Unpack like an ordinary tuple')
    x, y = p
    print(f'{x=}, {y=}')
    print('Create a new instance with _replace(); original is unchanged')
    moved = p._replace(x=10)
    print(f'{p=}, {moved=}')
    print('Convert fields to a dictionary with _asdict()')
    print(f'{p._asdict()=}')
    print(f'{Point._fields=}')
    print('Build from an iterable with _make()')
    another = Point._make([5, 6])
    print(f'{another=}')


def ordereddict_example():
    print('\n=== OrderedDict: ordered mapping with reordering tools ===')
    ordered = cl.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(f'{ordered=}')
    print('Move an existing item to the end')
    ordered.move_to_end('a')
    print(f'{list(ordered.items())=}')
    print('Move an item to the beginning')
    ordered.move_to_end('c', last=False)
    print(f'{list(ordered.items())=}')
    print('Remove the first item (FIFO)')
    removed = ordered.popitem(last=False)
    print(f'{removed=}, {ordered=}')

    print('Unlike regular dict equality, OrderedDict equality checks order')
    one = cl.OrderedDict([('x', 1), ('y', 2)])
    two = cl.OrderedDict([('y', 2), ('x', 1)])
    print(f'{one == two=}')
    print(f'{dict(one) == dict(two)=}')


def userdict_example():
    print('\n=== UserDict: easier customization of dictionary behavior ===')

    class UpperKeyDict(cl.UserDict):
        def __setitem__(self, key, value):
            super().__setitem__(str(key).upper(), value)

        def __getitem__(self, key):
            return super().__getitem__(str(key).upper())

    custom = UpperKeyDict()
    custom['color'] = 'blue'
    custom['size'] = 3
    print(f'{custom=}')
    print('The underlying regular dict lives in .data')
    print(f'{custom.data=}')
    print(f"{custom['COLOR']=}")
    print(f"{custom['color']=}")


def userlist_example():
    print('\n=== UserList: easier customization of list behavior ===')

    class LoggedList(cl.UserList):
        def append(self, item):
            print(f'LoggedList.append({item!r})')
            super().append(item)

    custom = LoggedList([1, 2])
    custom.append(3)
    print(f'{custom=}')
    print('The underlying regular list lives in .data')
    print(f'{custom.data=}')
    print(f'{custom[0]=}')
    print('Other standard list operations remain available')
    custom.reverse()
    print(f'{custom=}')


def userstring_example():
    print('\n=== UserString: easier customization of string behavior ===')

    class ShoutString(cl.UserString):
        def shout(self):
            return self.data.upper() + '!'

    custom = ShoutString('hello')
    print(f'{custom=}')
    print('The underlying regular string lives in .data')
    print(f'{custom.data=}')
    print(f'{custom.shout()=}')
    print(f'{custom.lower()=}')
    print('Strings are immutable: operations return new values')
    changed = custom.replace('h', 'j')
    print(f'{custom=}, {changed=}')


if __name__ == '__main__':
    main()
