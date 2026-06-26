
a = {1: '☝️', 2: '👀', 3: '🚦', 4: '🍀', 5: '🌸'}
print(a)                        # {1: '☝️', 2: '👀', 3: '🚦', 4: '🍀', 5: '🌸'}
print(len(a))                   # 5
print(2 in a)                   # True
print(a[2])                     # 👀
a[2] = '🂲' 
print(a)                        # {1: '☝️', 2: '🂲', 3: '🚦', 4: '🍀', 5: '🌸'}
try:
    print(a[6])
except KeyError as e:
    print(e)                    # KeyError: 6

del a[2]
value = a.pop(3)                # value:  '🚦'
print(a)                        # {1: '☝️', 4: '🍀', 5: '🌸'}
value = a.pop(6, 'not found')   # value: 'not found'
try:
    value = a.pop(6)
except KeyError as e:
    print(e)                    # KeyError: 6

print(a.keys())                 # dict_keys([1, 4, 5])
print(a.values())               # dict_values(['☝️', '🍀', '🌸'])
print(a.items())                # dict_items([(1, '☝️'), (4, '🍀'), (5, '🌸')])

a.update({2: '②', 3: '③'})
print(a)                        # {1: '☝️', 4: '🍀', 5: '🌸', 2: '②', 3: '③'}
b = a
a |= {2: 'Ⅱ', 3: 'Ⅲ'}
print(b)                        # {1: '☝️', 4: '🍀', 5: '🌸', 2: 'Ⅱ', 3: 'Ⅲ'}
a = a | {2: '➋', 3: '➌'}
print(b)                        # {1: '☝️', 4: '🍀', 5: '🌸', 2: 'Ⅱ', 3: 'Ⅲ'}
print(a)                        # {1: '☝️', 4: '🍀', 5: '🌸', 2: '➋', 3: '➌'}

a = {1: '☝️', 2: '👀'       }
b = {         2: '⚁', 3: '⚂'}
c = a | b
print(c)                        # {1: '☝️', 2: '⚁', 3: '⚂'}

smile = '😀'
love = '😍'
a = dict(smile=smile, love=love)
print(a)                        # {'smile': '😀', 'love': '😍'}

value = a.get('smile')
print(value)                    # 😀
value = a.get('sad', 'not found')
print(value)                    # not found

emos = ['😀', '😍', '😟', '😟', '😍']
indices = {}
for i, emo in enumerate(emos):
    indices.setdefault(emo, []).append(i)
print(indices)                  # {'😀': [0], '😍': [1, 4], '😟': [2, 3]}
for emo, idx in indices.items():
    print(f'{emo}: {idx}')      # 😀: [0]
                                # 😍: [1, 4]
                                # 😟: [2, 3]

import copy
a = {i: [] for i in range(2)}
print(a)                        # {0: [], 1: []}
c1 = a
c2 = a.copy()
c3 = copy.deepcopy(a)
a[2] = []
a[1].append('☝️')
print(c1)                       # {0: [], 1: ['☝️'], 2: []}
print(c2)                       # {0: [], 1: ['☝️']}
print(c3)                       # {0: [], 1: []}

fruit = ['🍓', '🍌', '🥝']
a = {'fruit': fruit}
print(a)                        # {'fruit': ['🍓', '🍌', '🥝']}
try:
    a[fruit] = 'fruit'
except TypeError as e:
    print(e)                    # unhashable type: 'list'
a[tuple(fruit)] = 'fruit'
print(a)                        # {'fruit': ['🍓', '🍌', '🥝'], ('🍓', '🍌', '🥝'): 'fruit'}

