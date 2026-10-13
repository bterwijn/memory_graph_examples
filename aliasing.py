
print("Aliasing in Python")
a = [1, 2, 3]
b = a
b.append(4)    # this changes 'b' and 'a'!
               # due to reference semantics and mutability
print(f"{a=}")
print(f"{b=}")
