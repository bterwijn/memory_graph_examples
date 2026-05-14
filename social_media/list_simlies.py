# show lists horizontally
mg.config.type_to_horizontal[list] = True

mylist = ['😀','😎','😍']

print(mylist)                    # ['😀','😎','😍']
mylist.append('😪')              # ['😀','😎','😍','😪']
print(mylist.count('😎'))        # 1
mylist_copy = mylist.copy()      # ['😀','😎','😍','😪']
print(mylist.index('😍'))        # 2
mylist.reverse()                 # ['😪','😍','😎','😀']
mylist.remove('😎')              # ['😪','😍','😀']
mylist.insert(1, '😜')           # ['😪','😜','😍','😀']
mylist.pop()                     # ['😪','😜','😍']
mylist.pop(1)                    # ['😪','😍']
mylist.extend(['😀','😎','😜'])  # ['😪','😍','😀','😎','😜']
mylist.sort()                    # ['😀','😍','😎','😜','😪']
mylist.clear()                   # []
