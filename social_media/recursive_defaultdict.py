from collections import defaultdict

# defaultdict uses factory to create default value of 
# give type if the key does't exists
mydict = defaultdict(list)
print(mydict["non existing key"])  # []

# lambda can be used recursively
factorial = lambda x : x * factorial(x-1) if x > 0 else 1
print(factorial(4))  # 24

# create a defaultdict but only at level 1
d = defaultdict(defaultdict)
try:
    print(d)        # defaultdict(<class 'collections.defaultdict'>, {})
    print(d[1])     # defaultdict(None, {})
    print(d[1][2])  # exception because factory is None
except Exception as e:
    print(e)  # KeyError 2

# create a defaultdict at any level recursively
tree = lambda: defaultdict(tree)

config = tree()
print(config[1])
print(config[1][2])  # defaultdict at any level

config["spark"]["sql"]["shuffle"]["partitions"] = 400
config["spark"]["sql"]["shuffle"]["xxx"] = 300
config["spark"]["sql"]["yyy"] = 200
config["A"]["B"]["C"] = 100

# no KeyError, levels appear as needed
