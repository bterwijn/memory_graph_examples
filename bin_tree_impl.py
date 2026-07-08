import random

class Bin_Tree_Nodes:
    def __init__(self):
       self.root = None

    def insert(self, data):
        def _insert(data, node):
            while True:
                if data < node.data:
                    if node.smaller is None:
                        node.smaller = Node(data)
                        break
                    else:
                        node = node.smaller
                else:
                    if node.larger is None:
                        node.larger = Node(data)
                        break
                    else:
                        node = node.larger
        if self.root is None:
            self.root = Node(data)
        else:
            _insert(data, self.root)

    def get_values(self):
        def _get_values(node):
            if node is None:
                return []
            return _get_values(node.smaller) + [node.data] + _get_values(node.larger)
        return _get_values(self.root)

class Node:
    def __init__(self, data):
        self.smaller = None
        self.data = data
        self.larger = None

class Bin_Tree_List:
    def __init__(self):
        self.values = []

    def insert(self, data):
        def _insert(index, data):
            while True:
                if index >= len(self.values):
                    self.values.extend([None]*(index - len(self.values) + 1))
                    self.values[index] = data
                    return
                elif self.values[index] == None:
                    self.values[index] = data
                    return
                elif data < self.values[index]:
                    index = 2*index + 1
                else:
                    index = 2*index + 2
        _insert(0, data)

    def get_values(self):
        def _get_values(index):
            if index >= len(self.values) or self.values[index] is None:
                return []
            return _get_values(2*index + 1) + [self.values[index]] + _get_values(2*index + 2)
        return _get_values(0)

bin_tree_nodes = Bin_Tree_Nodes()
bin_tree_list = Bin_Tree_List()
n = 10
for _ in range(n):
    data = random.randint(1, n*10)
    bin_tree_nodes.insert(data)
    bin_tree_list.insert(data)
print(f'bin_tree_nodes: {bin_tree_nodes.get_values()}')
print(f'bin_tree_list : {bin_tree_list.get_values()}')
