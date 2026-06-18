
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_List:
    
    def __init__(self):
        self.begin = None
        self.end = None
        
    def add(self, data):
        if self.begin == None:
            self.begin = Node(data)
            self.end = self.begin
        else:
            oldend = self.end 
            self.end = Node(data)
            oldend.next = self.end
            
linked_list = Linked_List()
for i in range(10):
    linked_list.add(i)

