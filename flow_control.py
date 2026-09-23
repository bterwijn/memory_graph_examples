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
def function_name(x, y):
    print(f'{x=} {y=}')
    result = x + y
    print(f'{result=}')
    return result

a = 10
b = 6
c = function_name(a, b)
print(f'{c=}')
