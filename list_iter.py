
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
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return Iterator_Forward(self.head)

    def backward_iter(self):
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

# build a linked list
linked_list = Linked_List()
for i in range(5):
    linked_list.insert_tail(i)

# forward iterate through the list and print values
for value in linked_list:
    print(value)

# backward iterate through the list and print values
# - this is what the for-loop does under the hood:
iter = linked_list.backward_iter()
try:
    while True:
        value = next(iter)
        print(value)
except StopIteration:
    pass # iteration finished
