
def p(x):
    print(x)


a = {'🍓', '🍌'} | {'🍌', '🍉'}; p(a)
a = {'🍓', '🍌'} & {'🍌', '🍉'}; p(a)
a = {'🍓', '🍌'} ^ {'🍌', '🍉'}; p(a)
a = {'🍓', '🍌'} - {'🍌', '🍉'}; p(a)


a = {'🍓', '🍌', '🍒', '🥥', '🍉', '🍍', '🥝', '🍎', '🍇'}

print()

a =  {'🍓', '🍌'}; p(a)
a |= {'🍌', '🍉'}; p(a)
a &= {'🍓', '🍌', '🍒'}; p(a)
a ^= {'🍓', '🥝'}; p(a)
a -= {'🍌', '🍇'}; p(a)

print()
a =  {'🍓', '🍌'}; p(a)
print('🍍' in a)
a.add('🍍'); p(a)
a.add('🍍'); p(a)
print('🍍' in a)
a.discard('🍍'); p(a)
a.discard('🥥'); p(a)
try:
    a.remove('🥥'); p(a)
except KeyError:
    print("not found")
