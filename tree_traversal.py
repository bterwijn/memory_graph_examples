import random
import string

class Node:
    def __init__(self, value):
        self.smaller = None
        self.value = value
        self.larger = None

    def insert(self, value):
        if value < self.value:
            if self.smaller:
                self.smaller.insert(value)
            else:
                self.smaller = Node(value)
        else:
            if self.larger:
                self.larger.insert(value)
            else:
                self.larger = Node(value)

    def preorder(self, prepend=None, indent=0, remove=-1):
        if remove >= 0:
            print()
            prepend[remove] = '  └'
            print(''.join(prepend), end='')
            prepend[remove] = ' ' * len(prepend[remove])
        print(f'──{self.value}', end='')
        prepend.append('  │' if self.smaller else '   ')
        if self.larger:
            self.larger.preorder(prepend, indent + 1)
        if self.smaller:
            self.smaller.preorder(prepend, indent + 1, indent)
        prepend.pop() 

    def inorder(self):
        if self.smaller:
            self.smaller.inorder()
        print(self.value, end=' ')
        if self.larger:
            self.larger.inorder()

    def postorder(self):
        smaller = self.smaller.postorder() if self.smaller else []
        larger = self.larger.postorder() if self.larger else []
        longest = smaller if len(smaller) > len(larger) else larger
        return [self.value] + longest

class BinTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def preorder(self):
        self.root.preorder([])
        print()

    def inorder(self):
        self.root.inorder()
        print()

    def postorder(self):
        print(self.root.postorder())

n = 8
values = list(string.ascii_lowercase[:n])
random.shuffle(values)
print('build binary tree with values: ', values)
bintree = BinTree()
for i in values:
    print(' insert:', i)
    bintree.insert(i)

print('\npreorder traversal: print full tree structure')
bintree.preorder()
    
print('\ninorder traversal: all values in sorted order')
bintree.inorder()

print('\npostorder traversal: longest path from root to leaf')
bintree.postorder()
