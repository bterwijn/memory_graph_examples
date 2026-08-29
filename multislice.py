

class MultiSlice:
    def __init__(self, values):
        self.values = values

    def __getitem__(self, keys):
        if not isinstance(keys, tuple):
            keys = (keys,)  # make it a tuple anyway
        container_type = type(self.values)
        result = container_type()  # empty container of same type
        for key in keys:
            if isinstance(key, slice):
                result += (self.values[key])
            elif isinstance(key, int):
                if isinstance(self.values, str):
                    result += self.values[key]
                else:
                    result += container_type((self.values[key],))
            else:
                raise TypeError(f"Invalid index type: {type(key).__name__}")
        return result

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Iterator:
    def __init__(self, node):
        self.current = node
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.step()
            return data

class Iterator_Forward(Iterator):
    def __init__(self, node):
        super().__init__(node)
        
    def step(self):
        self.current = self.current.next

class Iterator_Backward(Iterator):
    def __init__(self, node):
        super().__init__(node)
        
    def step(self):
        self.current = self.current.prev
    
class Linked_List:
    def __init__(self, iterable=tuple()):  # required
        self.head = None
        self.tail = None
        for i in iterable:
            self.insert_tail(i)

    def __iadd__(self, other):  # required
        for data in other:
            self.insert_tail(data)
        return self

    def __getitem__(self, slice_or_int):  # required
        if isinstance(slice_or_int, slice):  # slice
            return Linked_List(list(self)[slice_or_int])
        else:  # int
            i = slice_or_int
            iterator = iter(self) if i >= 0 else reversed(self)
            v = None
            for _ in range(abs(i)):
                v = next(iterator)
            return v
        
    def __repr__(self):
        return str([str(i) for i in self])

    def __iter__(self):
        return Iterator_Forward(self.head)

    def __reversed__(self):
        return Iterator_Backward(self.tail)      

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node

data = "0123456789"

a = MultiSlice(data)[0:3, 5, -3:-1]
b = MultiSlice(tuple(data))[0:3, 5, -3:-1]
c = MultiSlice(list(data))[0:3, 5, -3:-1]
d = MultiSlice(Linked_List(data))[0:3, 5, -3:-1]

print(a,b,c,d, sep='\n')
