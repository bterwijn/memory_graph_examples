
a = {'🍓','🍌'}         # a: {'🍓','🍌'}
print(len(a))           # 2
print('🥝' in a)        # False, complexity O(1)
a.add('🥝')             # a: {'🍓','🍌','🥝'}
a.add('🥝')             # a: {'🍓','🍌','🥝'}
print('🥝' in a)        # True, complexity O(1)
a.discard('🍌')         # a: {'🍓','🥝'}
a.discard('🍌')         # a: {'🍓','🥝'}
try:
    a.remove('🍌')      # a: {'🍓','🥝'}
except KeyError:
    print("not found")  # not found
a.clear()               # a: set()

a = {'🍓','🍓'} | {'🍓','🍓'};  # a: {'🍓'}
a = {'🍓','🍌'} | {'🍌','🍉'};  # a: {'🍓','🍌','🍉'}
a = {'🍓','🍌'} & {'🍌','🍉'};  # a: {'🍌'}
a = {'🍓','🍌'} ^ {'🍌','🍉'};  # a: {'🍓','🍉'}
a = {'🍓','🍌'} - {'🍌','🍉'};  # a: {'🍓'}

print({'🍓','🍌'} == {'🍌','🍓'})          # True
print({'🍓'}.issubset({'🍓','🍌'}))        # True
print({'🍓'} <=       {'🍓','🍌'})         # True
print({'🍓','🍌'}.issuperset({'🍓'}))      # True
print({'🍓','🍌'} >=         {'🍓'})       # True
print(    {'🍓','🍌'}.isdisjoint({'🍒'}))  # True
print(not {'🍓','🍌'} &          {'🍒'})   # True
