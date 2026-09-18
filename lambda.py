import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return self.name+':'+str(self.age)
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

names = ['Carol', 'Ann', 'Dave',  'Bob']    
people = [Person(n,random.randrange(100)) for n in names]
print('unsorted:', people)

sort_name = sorted(people, key= lambda p : p.get_name())
print('sort by name:', sort_name)

sort_age = sorted(people, key= lambda p : p.get_age())
print('sort by age:', sort_age)
