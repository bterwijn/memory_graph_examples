import random

class Heap_List:
    def __init__(self):
        self.heap = []

    def __bool__(self):
        return bool(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Heap_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __bool__(self):
        return self.size > 0

    def insert(self, value):
        new_node = Node(value)
        self.size += 1

        if self.root is None:
            self.root = new_node
            return

        parent, is_left_child = self._parent_for_index(self.size)
        if is_left_child:
            parent.left = new_node
        else:
            parent.right = new_node

        self._heapify_up(new_node)

    def extract_min(self):
        if self.root is None:
            return None

        min_value = self.root.value
        if self.size == 1:
            self.root = None
            self.size = 0
            return min_value

        last_node = self._node_at_index(self.size)
        self.root.value = last_node.value
        parent, is_left_child = self._parent_for_index(self.size)
        if is_left_child:
            parent.left = None
        else:
            parent.right = None
        self.size -= 1
        self._heapify_down(self.root)
        return min_value

    def _node_at_index(self, index):
        node = self.root
        for direction in bin(index)[3:]:
            node = node.left if direction == '0' else node.right
        return node

    def _parent_for_index(self, index):
        parent = self.root
        path = bin(index)[3:]
        for direction in path[:-1]:
            parent = parent.left if direction == '0' else parent.right
        return parent, path[-1] == '0'

    def _heapify_up(self, node):
        while node is not self.root:
            parent = self._node_at_index(self._index_of(node) // 2)
            if node.value >= parent.value:
                return
            node.value, parent.value = parent.value, node.value
            node = parent

    def _heapify_down(self, node):
        while node.left is not None:
            smallest_child = node.left
            if node.right is not None and node.right.value < smallest_child.value:
                smallest_child = node.right
            if node.value <= smallest_child.value:
                return
            node.value, smallest_child.value = smallest_child.value, node.value
            node = smallest_child

    def _index_of(self, target):
        def find(node, index):
            if node is target:
                return index
            if node.left is not None:
                result = find(node.left, index * 2)
                if result is not None:
                    return result
            if node.right is not None:
                return find(node.right, index * 2 + 1)
            return None

        return find(self.root, 1)

values = list(range(5))
random.shuffle(values)
heap_list = Heap_List()
heap_tree = Heap_Tree()
for value in values:
    print('insert:', value)
    heap_list.insert(value)
    heap_tree.insert(value)

while heap_list:
    value1 = heap_list.extract_min()
    value2 = heap_tree.extract_min()
    print('extract_min:', value1, value2)

