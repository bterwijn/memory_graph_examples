import random

age = random.randrange(120)  # random age

# if, elif, else
if age < 10:
    print('child')
elif age < 18:
    print('teen')
elif age < 100:
    print('adult')
else:
    print('centenarian')


i = -1
# while, break, continue
while i < 10:  # <== continue
    i+=1
    print(i)
    if i >= 8:
        break
    if i % 2 == 0:  # if i is even
        continue
    print('odd')
# <== break


myrange = range(10)  # create a range
print(f'{myrange=}')
mylist = list(myrange)  # convert to list
print(f'{mylist=}')

# for, break, continue
for i in myrange:  # <== continue
    print(i)
    if i >= 8:
        break
    if i % 2 == 0:  # if i is even
        continue
    print('odd')
# <== break


# def, return
def function_name(a, b):
    print(f'{a=} {b=}')
    a *= 10  # only change local 'a' variable
    b *= 10
    c = a + b
    print(f'{a=} {b=} {c=}')
    return c

a = 1
b = 5
c = function_name(a, b)
print(f'{a=} {b=} {c=}')  # global 'a' variable still unchanged
