# show sets horizontally
mg.config.type_to_horizontal[set] = True

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
except KeyError as e:
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

a = {'🍓','🍌'}        # a: {'🍓','🍌'}
b = a                  # b: {'🍓','🍌'}
c = a.copy()           # c: {'🍓','🍌'}
print(a is c)          # False, different identity
a |= {'🍌','🍉'}       # a: {'🍓','🍌','🍉'}
a &= {'🍓','🍉'}       # a: {'🍓','🍉'}
a ^= {'🍉','🥝','🍒'}  # a: {'🍓','🥝','🍒'}
a -= {'🍒','🍌'}       # a: {'🍓','🥝'}
print(a is b)          # True, same identity
a = a | {'🥝','🍒'}    # a: {'🍓','🥝','🍒'}
print(a is b)          # False, different identity
