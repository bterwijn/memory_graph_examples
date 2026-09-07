from typing import Any, Literal


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def get_value(self) -> Any:
        return self.value


class DoublyLinkedList:
    def __init__(self, value: Any) -> None:
        new_node: Node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length: int = 1

    def print_list(self) -> None:
        current: Node | None = self.head
        while current is not None:
            print(f"{current.value} ", end="")
            current = current.next
        print()

    # TC = O(1)
    def append(self, value: Any) -> Literal[True]:
        new_node: Node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore[union-attr]
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    # TC = O(1)
    def pop(self) -> Node | None:
        if self.head is None:
            return None

        temp: Node = self.tail # type: ignore[assignment]

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # type: ignore[union-attr]
            self.tail.next = None # type: ignore[union-attr]
            temp.prev = None

        self.length -= 1

        return temp 

    # TC = O(1)
    def prepend(self, value: Any) -> Literal[True]:
        new_node: Node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        return True

    # TC = O(1)
    def pop_start(self) -> Node | None:
        if self.head is None:
            return None

        temp: Node = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp

    # TC = O(n)
    def get(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None

        temp: Node = self.head # type: ignore[assignment]

        if index < self.length/2:
            for _ in range(index):
                temp = temp.next # type: ignore[assignment]
        else:
            temp = self.tail # type: ignore[assignment]
            for _ in range(self.length-1, index, -1):
                temp = temp.prev # type: ignore[assignment]

        return temp

    # TC = O(n)
    def set_value(self, index: int, value: Any) -> bool:
        req_node: Node | None = self.get(index)

        if req_node is not None:
            req_node.value = value
            return True
        
        return False

    # TC = O(n)
    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)

        new_node: Node = Node(value)
        before: Node = self.get(index-1) # type: ignore[assignment]
        after: Node = before.next # type: ignore[assignment]

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

        return True

    # TC = O(n)
    def remove(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_start()

        if index == self.length-1:
            return self.pop()

        temp: Node = self.get(index) # type: ignore[assignment]
        before: Node = temp.prev # type: ignore[assignment]
        after: Node = temp.next # type: ignore[assignment]

        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before

        self.length -= 1

        return temp

    def get_length(self) -> int:
        return self.length

# create
my_doubly_linked_list: DoublyLinkedList = DoublyLinkedList(5)
my_doubly_linked_list.print_list()

print()

# append
my_doubly_linked_list.append(10)
my_doubly_linked_list.print_list()

print()

# pop
print(my_doubly_linked_list.pop().get_value()) # type: ignore[union-attr]
print(my_doubly_linked_list.pop().get_value()) # type: ignore[union-attr]
print(my_doubly_linked_list.pop()) # No nodes

print()

# prepend
my_doubly_linked_list.prepend(10)
my_doubly_linked_list.prepend(5)
my_doubly_linked_list.print_list()

print()

# pop start
print(my_doubly_linked_list.pop_start().get_value()) # type: ignore[union-attr]
print(my_doubly_linked_list.pop_start().get_value()) # type: ignore[union-attr]
print(my_doubly_linked_list.pop_start()) # No nodes

print()

# None <- 5 <-> 10 <-> 15 <-> 20 <-> 25 -> None
for value in range(5, 26, 5):
    my_doubly_linked_list.append(value)

# get
print(my_doubly_linked_list.get(1).get_value()) # type: ignore[union-attr]
print(my_doubly_linked_list.get(3).get_value()) # type: ignore[union-attr]

print()

# set
my_doubly_linked_list.set_value(2, 0)
my_doubly_linked_list.print_list()

print()

# insert
my_doubly_linked_list.insert(0, 0)
my_doubly_linked_list.insert(my_doubly_linked_list.get_length(), 0)
my_doubly_linked_list.insert(4, 15)
my_doubly_linked_list.print_list()

print()

# remove
my_doubly_linked_list.remove(0)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(my_doubly_linked_list.get_length()-1)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
