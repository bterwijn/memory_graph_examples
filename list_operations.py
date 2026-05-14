# show lists horizontally
mg.config.type_to_horizontal[list] = True

a = ['😀','😎','😍']
b = a
c = a.copy()
print(a)               # ['😀','😎','😍']
a.append('😪')         # ['😀','😎','😍','😪']
print(a.count('😎'))   # 1
print(a.index('😍'))   # 2
print(len(a))          # 4
print('😎' in a)       # True
a.reverse()            # ['😪','😍','😎','😀']
a.remove('😎')         # ['😪','😍','😀']
a.insert(1, '😜')      # ['😪','😜','😍','😀']
a.pop()                # ['😪','😜','😍']
a.pop(1)               # ['😪','😍']
print(enumerate(a))    # [(0, '😪'), (1, '😍')]
a = a[:1]              # ['😪']
a.extend(['😀','😎'])  # ['😪','😀','😎']
a += ['😜','😍']       # ['😪','😀','😎','😜','😍']
a.sort()               # ['😀','😍','😎','😜','😪']
a = a[1:3]             # ['😍','😎']
a *= 2                 # ['😍','😎','😍','😎']
a.clear()              # []

