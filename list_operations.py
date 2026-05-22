import copy   

# show lists horizontally
mg.config.type_to_horizontal[list] = True

a = ['🌹','🪻']        # a: ['🌹','🪻']
a.append('🌼')         # a: ['🌹','🪻','🌼']
a.append('🌼')         # a: ['🌹','🪻','🌼','🌼']
print(len(a))          # 4
print('🌼' in a)       # True, complexity O(n)
print(a.count('🌼'))   # 2
print(a.index('🌹'))   # 0
a.remove('🌼')         # a: ['🌹','🪻','🌼']
i = a.pop()            # a: ['🌹','🪻']
i = a.pop(0)           # a:      ['🪻']

a.extend(['🌻','🪷'])  # a: ['🪻','🌻','🪷']
a.insert(1, '🍀')      # a: ['🪻','🍀','🌻','🪷']
a += ['🌹','🌸']       # a: ['🪻','🍀','🌻','🪷','🌹','🌸']

print(a[1])            # '🍀'
print(a[1:])           # ['🍀','🌻','🪷','🌹','🌸']
print(a[1:-1])         # ['🍀','🌻','🪷','🌹']
print(a[-2:0:-1])      # ['🌹','🪷','🌻','🍀']
a = a[::-2]            # a: ['🌸','🪷','🍀']

a.append(['🪻','🌹'])  # a: ['🌸','🌻','🍀', ['🪻','🌹']]
a.insert(1, a)         # a: ['🌸', [...],'🌻','🍀', ['🪻','🌹']]
a.clear()              # a: []

a = [['🌹','🪷'], ['🌻','🪻']]    # a: [['🌹','🪷'], ['🌻','🪻']]
c1 = a
c2 = a.copy()
c3 = copy.deepcopy(a)
print(a == c1, a == c2, a == c3)  # True True True
a[0][0] = '🌼'                    # a: [['🌼','🪷'], ['🌻','🪻']]
print(a == c1, a == c2, a == c3)  # True True False
a.reverse()                       # a: [['🌻','🪻'], ['🌼','🪷']]
print(a == c1, a == c2, a == c3)  # True False False
a = a + ['🍀']                    # a: [['🌻','🪻'], ['🌼','🪷'], '🍀']
print(a == c1, a == c2, a == c3)  # False False False
a.pop()                           # a: [['🌻','🪻'], ['🌼','🪷']]
i, j = a         # i: ['🌻','🪻']  j: ['🌼','🪷']

for i in enumerate(a):
    print(i)     # (0, ['🌻','🪻'])
                 # (1, ['🌼','🪷'])

a = ['🌹','🪻']  # a: ['🌹','🪻']
a *= 2           # a: ['🌹','🪻','🌹','🪻']
b = sorted(a)    # b: ['🌹','🌹','🪻','🪻']
a.sort()         # a: ['🌹','🌹','🪻','🪻']
